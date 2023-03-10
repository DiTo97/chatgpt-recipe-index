import pathlib
import typing

from setuptools import find_packages, setup


_ROOT = pathlib.Path(__file__).parent.resolve()


def _find_requirements() -> typing.List[str]:
    """It finds Python requirements in 'requirements.txt'"""
    filepath = _ROOT / "requirements.txt"

    with filepath.open("rt") as f:
        return f.read().splitlines()


def main() -> None:
    setup(
        author="Federico Minutoli",
        author_email="fede97.minutoli@gmail.com",
        description="A common library of data and ORM models of the recipe index",
        include_package_data=True,
        install_requires=_find_requirements(),
        name="recipe_database",
        packages=find_packages(),
        version="0.0.0",
    )


if __name__ == "__main__":
    main()
