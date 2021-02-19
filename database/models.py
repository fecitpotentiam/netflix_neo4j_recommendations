from neomodel import (StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom)


class Director(StructuredNode):
    name = StringProperty(unique_index=True)
    product = RelationshipFrom('Product', 'DIRECTED_BY')


class Actor(StructuredNode):
    name = StringProperty(unique_index=True)
    product = RelationshipTo('Product', 'ACTED_IN')


class Country(StructuredNode):
    name = StringProperty(unique_index=True)
    product = RelationshipFrom('Product', 'FILMED_IN')


class Genre(StructuredNode):
    name = StringProperty(unique_index=True)
    product = RelationshipFrom('Product', 'GENRE')


class Rating(StructuredNode):
    name = StringProperty(unique_index=True)
    product = RelationshipFrom('Product', 'RATING')


class Type(StructuredNode):
    name = StringProperty(unique_index=True)
    product = RelationshipFrom('Product', 'TYPE')


class Product(StructuredNode):
    show_id = StringProperty(unique_index=True)
    title = StringProperty()
    director = RelationshipTo(Director, 'DIRECTED_BY')
    actor = RelationshipFrom(Actor, 'ACTED_IN')
    country = RelationshipTo(Country, 'FILMED_IN')
    genre = RelationshipTo(Genre, 'GENRE')
    year = IntegerProperty()
    rating = RelationshipTo(Rating, 'RATING')
    duration = StringProperty()
    type = RelationshipTo(Type, 'TYPE')
    description = StringProperty()