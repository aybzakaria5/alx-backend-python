#!/usr/bin/env python3
"""task 100"""
from typing import Sequence, Union

def safe_first_element(lst: Sequence) -> Union[None, any]:
    """
    Function that returns the first element of a sequence if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
