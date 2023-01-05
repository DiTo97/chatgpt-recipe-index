"""
Utility functions for Python in general.
"""
from typing import Any


def exists(obj: Any) -> bool:
    """It checks whether a Python object is not None

    Parameters
    ----------
    obj
        The Python object

    Returns
    -------
    _
        True, if the object is not None
    """
    return obj is not None
