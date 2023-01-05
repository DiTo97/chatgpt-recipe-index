import pathlib

from recipe_indexer.utils.logging import init_logging_queue


ROOT = pathlib.Path(__file__).parent.resolve()
"""The Python package root"""

DIRPATH_resources = ROOT / "resources"
"""The Python package resources dirpath"""

DIRPATH_config = DIRPATH_resources / "config"
"""The Python package sub-resources config dirpath"""


# It sets up the Python root logger
init_logging_queue()
