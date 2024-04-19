#!/usr/bin/env python3
"""task 8 """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """using Callable from typing"""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
