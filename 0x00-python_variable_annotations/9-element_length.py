#!/usr/bin/env python3
"""task 9"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes a list of sequences and returns a list of tuples
    where each tuple contains an element from the input list
    along with its length.
    """
    return [(i, len(i)) for i in lst]
