"""
Utility functions for Python args parsing.
"""
import argparse
import os
import yaml
from typing import Any

from recipe_indexer import DIRPATH_config
from recipe_indexer.utils.commons import exists
from recipe_indexer.utils.asyncio import gather
from recipe_indexer.utils.dict import merge_dicts


async def _load_config_yaml(name: str = "default") -> dict[Any, Any]:
    """It loads a config dict from a YAML resource file.

    The default YAML file is 'default.yml'.

    Raises
    ------
    FileNotFoundError
        If `name` == 'default' and 'default.yml' does not exist
    """
    filename = f"{name}.yml"
    filepath = DIRPATH_config / filename

    config = None

    try:
        with filepath.open("rt") as f:
            config = yaml.load(f, yaml.SafeLoader)
    except FileNotFoundError:
        if name == "default":
            raise

    if not exists(config):
        return {}

    return config


async def parse_args() -> tuple[str, bool, dict[Any, Any]]:
    """It parses the following Python package args:

    - the Python environment:
        1. by the '-e', or '--environment', CLI arg;
        2. by the 'ENVIRONMENT' env variable.

    The default Python environment is 'local'.

    - the Python verbose mode:
        1. by the '-v', or '--verbose', CLI arg;
        2. by the 'VERBOSE' env variable.

    The default Python verbose mode is False.

    It loads the Python config from specific YAML resource files.

    Returns
    -------
    environment
        The Python environment

    verbose
        Whether Python is in verbose mode

    config
        The Python config
    """
    DEFAULT_environment = os.getenv("ENVIRONMENT", "local")
    DEFAULT_verbose = bool(os.getenv("VERBOSE", False))

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-e", 
        "--environment", 
        default=DEFAULT_environment, 
        help="The Python environment"
    )

    parser.add_argument(
        "-v", 
        "--verbose", 
        default=DEFAULT_verbose, 
        action="store_true", 
        help="Whether Python is in verbose mode"
    )

    args, _ = parser.parse_known_args()

    environment = args.environment
    verbose = args.verbose

    coroutines = [
        _load_config_yaml(),
        _load_config_yaml(environment)
    ]

    config = merge_dicts(
        await gather(*coroutines)
    )

    return environment, verbose, config
