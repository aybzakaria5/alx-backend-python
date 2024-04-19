#!/usr/bin/env python3
"""task 100"""
from typing import Sequence, Union, Any

def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Function that returns the first element of a sequence if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
