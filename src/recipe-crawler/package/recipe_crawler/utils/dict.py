"""
Utility functions for Python dictionaries.
"""
from typing import Any


def merge_dicts(
    O: dict[Any, Any], N: dict[Any, Any], merge_lists: bool = False
) -> dict[Any, Any]:
    """It merges two dictionaries prioritizing the 2nd one

    Parameters
    ----------
    O
        The 1st dictionary

    N
        The 2nd dictionary

    merge_lists
        Whether lists should be merged or replaced

    Returns
    -------
    merged
        The merged dictionary
    """
    # It makes a shallow copy of O
    merged = O.copy()

    # It joins all keys
    O_keys = O.keys()
    N_keys = N.keys()

    keys = set(O_keys).union(set(N_keys))

    # It merges on each key
    for k in keys:
        # If the key is just in N, add it to merged...
        if k not in O_keys:
            merged[k] = N[k]
            continue
        # ...else if the key is in both dicts:
        elif k in N_keys:
            # If the values are both dicts, merge them recursively...
            if isinstance(O[k], dict) and isinstance(N[k], dict):
                merged[k] = merge_dicts(O[k], N[k], merge_lists)
            else:
                # ...else if merge_lists is True and the values are both lists,
                # concatenate all elements into O and N...
                if merge_lists and isinstance(O[k], list) and isinstance(N[k], list):
                    merged[k] = O[k] + N[k]
                # ...else keep the value in N
                else:
                    merged[k] = N[k]

    return merged
