import json

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

import requests

api_key = Variable.get("api_key_nasa")


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'alex',
}


@dag(default_args=default_args,
     schedule_interval=None,
     start_date=days_ago(2),
     tags=['example'])
def throwback_mission():
    """
    ### A short and sweet throwback in time.
    This is a simple ETL data pipeline will throw you back in time with
    historic imagery from planet mars. It queries our faviourite mars rover
    curiosity.

    [https://api.nasa.gov/#mars-rover-photos](https://api.nasa.gov/#mars-rover-photos)
    """
    @task()
    def extract():
        """
        #### Extract task
        Extracting all image data for a specific sol (mars day)
        """
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=DEMO_KEY'
        r = requests.get(url)
        images_sol = json.loads(r.text)
        return images_sol

    @task(multiple_outputs=True)
    def transform(images_sol: dict):
        """
        #### Transform task
        Get only the first image of the day, discard all others
        """
        list(images_sol.keys())[0]

        return {"total_order_value": total_order_value}

    @task()
    def load(total_order_value: float):
        """
        #### Load task
        A simple Load task which takes in the result of the Transform task and
        instead of saving it to end user review, just prints it out.
        """

        print("The image URL is: %.2f" % total_order_value)
    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])


tutorial_etl_dag = tutorial_taskflow_api_etl()
