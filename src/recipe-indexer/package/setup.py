import pathlib
from setuptools import find_packages, setup


_ROOT = pathlib.Path(__file__).parent.resolve()


def _find_requirements() -> list[str]:
    """It finds Python requirements in 'requirements.txt'"""
    filepath = _ROOT / "requirements.txt"

    with filepath.open("rt") as f:
        return f.read().splitlines()


def _find_resources_paths() -> list[str]:
    """It finds resources paths under 'recipe_indexer/resources/'"""
    dirname = "recipe_indexer"
    dirpath = _ROOT / dirname / "resources"

    return [str(r.relative_to(dirpath)) for r in dirpath.rglob("*")]


def main():
    setup(**{
        "author": "Federico Minutoli",
        "author_email": "fede97.minutoli@gmail.com",
        "description": "A ChatGPT-based indexer of recipes on the Internet",
        "install_requires": _find_requirements(),
        "name": "recipe_indexer",
        "packages": find_packages(),
        "package_data": {
            "recipe_indexer": _find_resources_paths(),
            "tests": ["stubs/*"]
        },
        "version": "0.1.0",
    })


if __name__ == "__main__":
    main()
