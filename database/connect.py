import os

from dotenv import load_dotenv
from neomodel import db
from py2neo import Graph


def get_url():
    dotenv_path = os.path.join(os.path.dirname(os.curdir), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    username = os.environ["NEO4J_USERNAME"]
    password = os.environ["NEO4J_PASSWORD"]
    url = f'bolt://{username}:{password}@localhost:7687'

    return url


def neomodel_connect():
    url = get_url()
    db.set_connection(url)

    return db


def py2neo_connect():
    url = get_url()
    return Graph(url)
