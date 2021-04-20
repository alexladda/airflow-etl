from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from airflow.hooks.base import BaseHook

from include.model_weather_station import Weather as Weather

conn = BaseHook.get_connection('aws_database')
engine = create_engine(conn.get_uri())
Session = sessionmaker(bind=engine)


def create_table():
    Weather.metadata.create_all(engine)


def reset_table():
    Weather.metadata.drop_all(engine)
    Weather.metadata.create_all(engine)


def rm_table():
    Weather.metadata.drop_all(engine)
