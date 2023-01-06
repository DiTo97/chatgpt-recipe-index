"""
This type stub file was generated by pyright.
"""

import typing
from sqlmodel import SQLModel

class Dosage_base(SQLModel):
    """A SQL model that maps the dosage of any ingredient in any recipe (base)"""
    quantity: typing.Optional[float] = ...
    unit_of_measure: typing.Optional[str] = ...
    ingredient: Ingredient = ...
    recipe: Recipe = ...


class Dosage_create(Dosage_base):
    """A SQL model that maps the dosage of any ingredient in any recipe (create)"""
    ...


class Dosage_read(Dosage_base):
    """A SQL model that maps the dosage of any ingredient in any recipe (read)"""
    ingredient_id: int
    recipe_id: int
    ...


class Dosage(Dosage_base, table=True):
    """A SQL model that maps the dosage of any ingredient in any recipe"""
    ingredient_id: typing.Optional[int] = ...
    recipe_id: typing.Optional[int] = ...


class Ingredient_base(SQLModel):
    """A SQL model that characterizes an ingredient (base)"""
    name: str = ...
    dosages: typing.List[Dosage] = ...


class Ingredient_create(Ingredient_base):
    """A SQL model that characterizes an ingredient (create)"""
    ...


class Ingredient_read(Ingredient_base):
    """A SQL model that characterizes an ingredient (read)"""
    id: int
    ...


class Ingredient(Ingredient_base, table=True):
    """A SQL model that characterizes an ingredient"""
    id: typing.Optional[int] = ...


class Recipe_base(SQLModel):
    """A SQL model that characterizes a recipe (base)"""
    name: str = ...
    type: str = ...
    preparation: str
    score: typing.Optional[float] = ...
    timedelta: typing.Optional[int] = ...
    dosages: typing.List[Dosage] = ...


class Recipe_create(Recipe_base):
    """A SQL model that characterizes a recipe (create)"""
    ...


class Recipe_read(Recipe_base):
    """A SQL model that characterizes a recipe (read)"""
    id: int
    ...


class Recipe(Recipe_base, table=True):
    """A SQL model that characterizes a recipe"""
    id: typing.Optional[int] = ...


