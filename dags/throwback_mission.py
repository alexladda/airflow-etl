import json

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

import requests

from airflow.models import Variable
api_key = Variable.get("api_key_nasa")


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'alex',
}


@dag(default_args=default_args,
     schedule_interval='@daily',
     start_date=days_ago(0),
     tags=['example'])
def throwback_mission():
    """
    # A short and sweet throwback in time.
    This is a simple ETL data pipeline will throw you back in time with
    historic imagery from planet mars. It queries our faviourite mars rover
    curiosity. It landed on 6 August 2012, 05:17:57 UTC / MSD 49269,
    05:53 AMT / MSD 49269, 14:53 LMST (Sol 0).

    This here will throw us back to exactly 9 years ago, aquiring the all
    images the rover took on that exact day. The script will store the image
    URLs in a consise table, replacing the values every day.

    On the frontend one random image will be selected and shown on each
    impression of the page.

    [More infos on the API](https://api.nasa.gov/#mars-rover-photos)
    """
    @task()
    def extract():
        """
        # Extract task
        Extracting all image data for a specific sol (mars day)
        """
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
        # a limited amount of queries is possible with this key:
        # api_key = 'DEMO_KEY'
        api_key = Variable.get("api_key_nasa")
        sol = 0
        payload = {'sol': sol, 'api_key': api_key}
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
        r = requests.get(url, params=payload)
        images_sol = json.loads(r.text)
        # returning the whole requests content
        return {'images_sol': json.loads(r.text)

    @ task(multiple_outputs=True)
    def transform(images_sol: dict):
        """
        # Transform task
        Get only the first image of the day, discard all others
        """
        image_url = list(images_sol.keys())[0]

        return {"image url": image_url}

    @ task()
    def load(image_url: string):
        """
        # Load task
        A simple Load task which takes in the result of the Transform task and
        instead of saving it to end user review, just prints it out.
        """

        print("The image URL is: %.2f" % total_order_value)

    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])


tutorial_etl_dag = tutorial_taskflow_api_etl()
