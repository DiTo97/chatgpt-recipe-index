from functools import lru_cache

from sqlalchemy.engine import Engine
from sqlmodel import SQLModel
from sqlmodel import create_engine as sqlmodel_create_engine

from recipe_database.datamodels import Dosage, Ingredient, Recipe
from recipe_database.typing_ import str_or_URL


@lru_cache
def create_engine(url: str_or_URL) -> Engine:
    """It creates a SQL engine connected to the database at the given URL

    All created engines are stored in a cache for future re-use
    """
    return sqlmodel_create_engine(url)


def create_database_and_tables(engine: Engine) -> None:
    """It creates database and tables for the recipe index given the SQL engine

    They are created only if they do not already exist.
    """
    SQLModel.metadata.create_all(engine)
