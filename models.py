from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom, config


class Product(StructuredNode):
    show_id = StringProperty(unique_index=True)
    title = StringProperty()
    directors = RelationshipTo('Director', 'DIRECTOR')
    actors = RelationshipTo('Actor', 'ACTOR')
    countries = RelationshipTo('Country', 'COUNTRY')
    genres = RelationshipTo('Genre', 'GENRE')
    year = IntegerProperty()
    rating = StringProperty()
    duration = StringProperty()
    description = StringProperty()


class Director(StructuredNode):
    name = StringProperty(unique_index=True)
    products = RelationshipFrom('Product', 'PRODUCT')


class Actor(StructuredNode):
    name = StringProperty(unique_index=True)
    products = RelationshipFrom('Product', 'PRODUCT')


class Country(StructuredNode):
    name = StringProperty(unique_index=True)
    products = RelationshipFrom('Product', 'PRODUCT')


class Genre(StructuredNode):
    name = StringProperty(unique_index=True)
    products = RelationshipFrom('Product', 'PRODUCT')
