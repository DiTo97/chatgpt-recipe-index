# pip imports
import os
import yaml

from argparse import ArgumentParser

from typing import Any

# Module imports
from recipe_api import DIRPATH_config
from recipe_api.utils.util_dict import merge_dicts


def _get_config_dict(env: str) -> dict[Any, Any]:
    """
    Get the config dict from YAML resource files.

    The default YAML file is `default.yml`.

    Raises
    ------
    FileNotFoundError
        If `env` == 'default' and `default.yml` does not exist
    """
    cfg_dict = None

    filename = f'{env}.yml'
    filepath = os.path.join(DIRPATH_config, filename)

    try:
        with open(filepath) as f:
            cfg_dict = yaml.load(f, yaml.SafeLoader)
    except FileNotFoundError as e:
        if env == 'default':
            raise e

    return cfg_dict if cfg_dict else {}


def _get_env() -> str:
    """
    Get the calling Python environment:
        1. by the '-e', or '--environment', CLI arg;
        2. by the 'py_ENVIRONMENT' env variable.

    It defaults to 'local'.
    """
    DEFAULT_env = os.getenv('py_ENVIRONMENT', 'local')

    parser = ArgumentParser()
    parser.add_argument('-e', '--environment',
                        default=DEFAULT_env,
                        help='The calling Python environment')

    args, _ = parser.parse_known_args()
    return args.environment


def _get_verbose() -> bool:
    """
    Get whether the Python execution is verbose:
        1. by the '-v', or '--verbose', CLI arg;
        2. by the 'py_VERBOSE' env variable.
    """
    DEFAULT_verbose = bool(os.getenv('py_VERBOSE', False))

    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose',
                        default=DEFAULT_verbose,
                        action='store_true',
                        help='Whether the Python execution is verbose')

    args, _ = parser.parse_known_args()
    return args.verbose


# Global variables
environment = _get_env()
"""
The calling Python environment
"""

verbose = _get_verbose()
"""
Whether the Python execution is verbose 
"""

cfg = merge_dicts(
    _get_config_dict('default'),
    _get_config_dict(environment)
)
"""
Package config
"""
