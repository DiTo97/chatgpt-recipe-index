import typing

from sqlmodel import Field, Relationship, SQLModel


class Dosage_base(SQLModel):
    """A SQL model that maps the dosage of any ingredient in any recipe (base)"""

    quantity: typing.Optional[float] = Field(default=None, gt=0.0)
    unit_of_measure: typing.Optional[str] = None

    ingredient: "Ingredient" = Relationship(back_populates="dosages")
    recipe: "Recipe" = Relationship(back_populates="dosages")


class Dosage_create(Dosage_base):
    """A SQL model that maps the dosage of any ingredient in any recipe (create)"""


class Dosage_read(Dosage_base):
    """A SQL model that maps the dosage of any ingredient in any recipe (read)"""

    ingredient_id: int
    recipe_id: int


class Dosage(Dosage_base, table=True):
    """A SQL model that maps the dosage of any ingredient in any recipe"""

    ingredient_id: typing.Optional[int] = Field(
        default=None,
        description="The unique Id of the ingredient",
        foreign_key="ingredient.id",
        primary_key=True,
    )

    recipe_id: typing.Optional[int] = Field(
        default=None,
        description="The unique Id of the recipe",
        foreign_key="recipe.id",
        primary_key=True,
    )


class Ingredient_base(SQLModel):
    """A SQL model that characterizes an ingredient (base)"""

    name: str = Field(index=True, unique=True)

    dosages: typing.List[Dosage] = Relationship(back_populates="ingredient")


class Ingredient_create(Ingredient_base):
    """A SQL model that characterizes an ingredient (create)"""


class Ingredient_read(Ingredient_base):
    """A SQL model that characterizes an ingredient (read)"""

    id: int


class Ingredient(Ingredient_base, table=True):
    """A SQL model that characterizes an ingredient"""

    id: typing.Optional[int] = Field(default=None, primary_key=True)


class Recipe_base(SQLModel):
    """A SQL model that characterizes a recipe (base)"""

    name: str = Field(index=True, unique=True)
    type: str = Field(index=True)
    preparation: str
    score: typing.Optional[float] = Field(default=None, ge=0.0, le=5.0)
    timedelta: typing.Optional[int] = Field(default=None, gt=0)

    dosages: typing.List[Dosage] = Relationship(back_populates="recipe")


class Recipe_create(Recipe_base):
    """A SQL model that characterizes a recipe (create)"""


class Recipe_read(Recipe_base):
    """A SQL model that characterizes a recipe (read)"""

    id: int


class Recipe(Recipe_base, table=True):
    """A SQL model that characterizes a recipe"""

    id: typing.Optional[int] = Field(default=None, primary_key=True)
