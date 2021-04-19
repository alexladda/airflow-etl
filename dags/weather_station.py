from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.models import Variable

import requests
import json


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'alex'
}


@dag(default_args=default_args,
     start_date=days_ago(2),
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

        r = requests.get(url, params=payload)
        print(r)
        raw_weather = json.loads(r.text)
        print("*** RAW WEATHER ***")
        print(raw_weather)

        return raw_weather

    @task(multiple_outputs=True)
    def transform(raw_weather: dict):
        """
        #### Transform task
        # TODO: check if null etc... let's see what comes in.
        """

        # for now do nothing
        weather_now = raw_weather

        print("*** WEATHER NOW ***")
        pretty = json.dumps(weather_now, indent=2)
        print(pretty)

        return weather_now

    @task()
    def load(weather_now: dict):
        """
        #### Load task
        # TODO: commit to db
        """

        print("*** COMMIT ****")
        print("*** DB Connection ****")
        for item in weather_now:
            print(item)

    raw_weather = extract()
    weather_now = transform(raw_weather)
    load(weather_now)


weather_station_dag = weather_station()
