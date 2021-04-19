from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from airflow.hooks.base import BaseHook


conn = BaseHook.get_connection('aws_database_1')
# engine = create_engine(conn)
# Session = sessionmaker(bind=engine)


def create_database(Model):
    Model.metadata.create_all(engine)


def reset_database(Model):
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)


def rm_database(Model):
    Model.metadata.drop_all(engine)
