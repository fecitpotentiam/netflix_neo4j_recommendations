from typing import List

import pandas as pd
from neomodel.core import NodeBase

from database.connect import neomodel_connect
from database.models import Product, Director, Actor, Country, Genre, Rating, Type


class Importer:
    def __init__(self):
        self.db = neomodel_connect()
        self.dataframe = pd.read_csv('data/netflix_titles.csv')

    @staticmethod
    def __create_relationship(
            product: Product,
            elements: List[str],
            model_cls: NodeBase,
            connection_name: str
    ) -> None:
        for element_name in elements:
            if element_name != 'nan':
                connected_object = model_cls.get_or_create({'name': element_name})[0]
                product.__getattribute__(connection_name).connect(connected_object)

    @staticmethod
    def __split_row(row, columns_list: List[str]):
        return [(str(row[column_name])).split(', ') for column_name in columns_list]

    def import_data(self):
        for index, row in self.dataframe.iterrows():
            directors, actors, countries, genres = self.__split_row(
                row,
                ['director', 'cast', 'country', 'listed_in']
            )

            product = Product(
                show_id=row['show_id'],
                title=row['title'],
                year=int(row['release_year']),
                description=row['duration'],
                duration=row['duration']
            ).save()

            self.__create_relationship(product, directors, Director, 'director')
            self.__create_relationship(product, actors, Actor, 'actor')
            self.__create_relationship(product, countries, Country, 'country')
            self.__create_relationship(product, genres, Genre, 'genre')
            self.__create_relationship(product, [row['rating']], Rating, 'rating')
            self.__create_relationship(product, [row['type']], Type, 'type')

            print(row['title'], 'imported', index, 'of', len(self.dataframe))

        print('Import has finished')


if __name__ == '__main__':
    importer = Importer()
    importer.import_data()
