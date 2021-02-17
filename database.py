import os

from dotenv import load_dotenv
from neomodel import db


def connect():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    username = os.environ["NEO4J_USERNAME"]
    password = os.environ["NEO4J_PASSWORD"]

    db.set_connection(f'bolt://{username}:{password}@localhost:7687')

    return db
