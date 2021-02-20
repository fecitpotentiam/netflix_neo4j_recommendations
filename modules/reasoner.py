from typing import List

from database.connect import py2neo_connect

QUERY_RETURN_STRING = " RETURN DISTINCT rec ORDER BY -rec.year LIMIT %d"


class Reasoner:
    def __init__(self):
        self.graph = py2neo_connect()

    @staticmethod
    def __get_relationship(param: str) -> str:
        return f"-->(:{param})<--" if param != 'Actor' else f"<--(:{param})-->"

    def __create_first_level_query(self, param: str) -> str:
        return "(rec:Product)" + self.__get_relationship(param) + "(:Product {title: '%s'})"

    def __create_second_level_query(self, param: str) -> str:
        return "(:Product {title: '%s'})" + self.__get_relationship(param)

    def __create_query(self, title: str, limit: int, params: List[str]) -> str:
        first_level_query = self.__create_first_level_query(params[0]) % title + QUERY_RETURN_STRING % limit

        if len(params) == 1:
            return "MATCH " + first_level_query
        elif len(params) == 2:
            return "MATCH " + self.__create_second_level_query(params[1]) % title + first_level_query
        else:
            raise ValueError("Too many params (works only with one or two params)")

    def get_recommendations(self, title: str, params: List[str], limit: int = 20) -> List[str]:
        query = self.__create_query(title, limit, params)

        return [product['rec']['title'] for product in self.graph.run(query).data()]


if __name__ == '__main__':
    reasoner = Reasoner()
    print(reasoner.get_recommendations('The Witcher', ['Actor'], 20))