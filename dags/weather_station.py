from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.models import Variable


import requests
import json

import include.crud_weather_station as c
from include.model_weather_station import Weather as Weather


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'alex'
}


@dag(default_args=default_args,
     start_date=days_ago(0),
     schedule_interval='*/5 * * * *')
def weather_station():
    """
    ### Ahoi

    Check the wind before you set sail.
    """
    @task()
    def extract():
        """
        #### Extract task
        Fetching weather data for a specific location.
        """
        url = 'https://api.openweathermap.org/data/2.5/weather'
        api_key = Variable.get("api_key_openweather")
        payload = {'lat': -8.663794, 'lon': 115.135669, 'APPID': api_key}

        raw_weather = requests.get(url, params=payload)
        print("*** RAW WEATHER ***")
        print(raw_weather)
        print(raw_weather.text)
        return {'raw_weather': json.loads(raw_weather.text)}

    @task(multiple_outputs=True)
    def transform(raw_weather: dict):
        """
        #### Transform task
        # <transform json dict to list of values for the class>
        # TODO: check if null etc... let's see what comes in.
        """

        w_data = raw_weather['raw_weather']

        print("****** WEATHER NOW <start> ******")
        pretty = json.dumps(w_data, indent=2)
        print(pretty)
        print("****** WEATHER NOW <end>   ******")

        print("****** PARSING WEATHER <start> ******")
        # initializing dict
        w_now = {}

        # TODO: try, except dict key error
        # commented out lines likely to not be in json
        w_now['coord_lon'] = w_data['coord']['lon']
        w_now['coord_lat'] = w_data['coord']['lat']
        w_now['weather_id'] = w_data['weather'][0]['id']
        w_now['weather_main'] = w_data['weather'][0]['main']
        w_now['weather_description'] = w_data['weather'][0]['Clouds']
        w_now['weather_icon'] = w_data['weather'][0]['description']
        w_now['base_source'] = w_data['main']
        w_now['main_temp'] = w_data['main']['temp']
        w_now['main_feels_like'] = w_data['main']['feels_like']
        w_now['main_temp_min'] = w_data['main']['temp_min']
        w_now['main_temp_max'] = w_data['main']['temp_max']
        w_now['main_pressure'] = w_data['main']['pressure']
        w_now['main_humidity'] = w_data['main']['humidity']
        # w_now['main_sea_level'] = w_data['main']['sea_level']
        # w_now['main_ground_level'] = w_data['main']['grnd_level']
        w_now['visibility'] = w_data['visibility']
        # w_now['precipation_value'] = w_data['precipation']['value']
        # w_now['precipation_mode'] = w_data['precipation']['mode']
        # w_now['rain_1h'] = w_data['rain']['1h']
        # w_now['rain_3h'] = w_data['rain']['3h']
        # w_now['snow_1h'] = w_data['snow']['1h']
        # w_now['snow_3h'] = w_data['snow']['3h']
        w_now['wind_speed'] = w_data['wind']['speed']
        w_now['wind_deg'] = w_data['wind']['deg']
        # w_now['wind_gust'] = w_data['wind']['gust']
        w_now['clouds_all'] = w_data['clouds']['all']
        w_now['dt'] = w_data['dt']
        w_now['sys_type'] = w_data['sys']['type']
        w_now['sys_id'] = w_data['sys']['id']
        w_now['sys_country'] = w_data['sys']['country']
        w_now['sys_sunrise'] = w_data['sys']['sunrise']
        w_now['sys_sunset'] = w_data['sys']['sunset']
        w_now['timezone'] = w_data['timezone']
        w_now['city_id'] = w_data['id']
        w_now['city_name'] = w_data['name']
        w_now['cod'] = w_data['cod']

        print("****** PARSING WEATHER <end> ******")
        return w_now

    @task()
    def load(w_now: dict):
        """
        #### Load task
        # TODO: instantiate Weather class, commit to db
        """

        Weather_now = Weather(**w_now)
        print("*** DB Connection ****")
        s = c.Session()
        s.add(Weather_now)
        print("*** COMMIT ****")
        s.commit()
        s.close()

    raw_weather = extract()
    w_now = transform(raw_weather)
    load(w_now)


weather_station_dag = weather_station()
