import typing

from sqlmodel import Field, Relationship, SQLModel


class Dosage(SQLModel, table=True):
    """A SQL model that maps the dosage of any ingredient in any recipe"""

    recipe_id: typing.Optional[int] = Field(
        default=None,
        description="The unique Id of the recipe",
        foreign_key="recipe.id",
        primary_key=True,
    )

    ingredient_id: typing.Optional[int] = Field(
        default=None,
        description="The unique Id of the ingredient",
        foreign_key="ingredient.id",
        primary_key=True,
    )

    quantity: typing.Optional[str] = None

    recipe: "Recipe" = Relationship(back_populates="dosages")
    ingredient: "Ingredient" = Relationship(back_populates="dosages")


class Recipe(SQLModel, table=True):
    """A SQL model that characterizes a recipe"""

    id: typing.Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    type: str = Field(index=True)
    preparation: str
    score: typing.Optional[float] = Field(default=None, ge=0.0, le=5.0)
    timedelta: typing.Optional[int] = Field(default=None, gt=0)

    dosages: typing.List[Dosage] = Relationship(back_populates="recipe")


class Ingredient(SQLModel, table=True):
    """A SQL model that characterizes an ingredient"""

    id: typing.Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)

    dosages: typing.List[Dosage] = Relationship(back_populates="ingredient")
