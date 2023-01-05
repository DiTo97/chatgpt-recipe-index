# pip imports
import os

from setuptools import (
    find_packages,
    setup
)


def _get_requirements() -> list[str]:
    """
    Get all package requirements.
    """
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'requirements.txt'
    )

    with open(filepath, 'rt') as f:
        return f.read().splitlines()


def _get_resources(package: str) -> list[str]:
    """
    Get all package resources filepaths.

    Parameters
    ----------
    package : str
        The package name
    """
    resources = [os.path.join(pkg, filename)
                 for pkg, _, filenames
                     in os.walk(os.path.join(package, 'resources'))
                 for filename in filenames]

    # Remove the package name from filepaths
    return [r[r.index('resources'):] for r in resources]


if __name__ == '__main__':
    # Package configuration
    setup(**{
        'author': 'Federico Minutoli',
        'author_email': 'fede97.minutoli@gmail.com',
        'description': 'A FastAPI API to query the recipe index',
        'install_requires': _get_requirements(),
        'name': 'recipe_api',
        'packages': find_packages(),
        'package_data': {
            'recipe_api': _get_resources('recipe_api'),
            'tests': ['stubs/*']
        },
        'version': '0.1.0',
    })
