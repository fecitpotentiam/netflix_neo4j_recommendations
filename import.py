import pandas as pd
from database import connect

from models import Product, Director, Actor, Country, Genre

db = connect()

dataframe = pd.read_csv('data/netflix_titles.csv')


def create_relationship(product, elements, model_cls, connection_name):
    for element_name in elements:
        if str(element_name) != 'nan':
            e = model_cls.nodes.get_or_none(name=element_name)
            if not e:
                e = model_cls(name=element_name).save()

            product.__getattribute__(connection_name).connect(e)


def import_data():
    for index, row in dataframe.iterrows():
        directors = str(row['director']).split(', ')
        actors = str(row['cast']).split(', ')
        countries = str(row['country']).split(', ')
        genres = str(row['listed_in']).split(', ')

        product = Product(
            show_id=row['show_id'],
            title=row['title'],
            year=int(row['release_year']),
            rating=row['rating'],
            description=row['duration'],
            duration=row['duration']
        ).save()

        create_relationship(product, directors, Director, 'directors')
        create_relationship(product, actors, Actor, 'actors')
        create_relationship(product, countries, Country, 'countries')
        create_relationship(product, genres, Genre, 'genres')

        print(row['title'], 'imported', index, 'of', len(dataframe))


import_data()
