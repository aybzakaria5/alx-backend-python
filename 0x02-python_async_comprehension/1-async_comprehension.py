#!/usr/bin/env python3

"""
This module contains a function that
performs an asynchronous comprehension.

The async_comprehension function
uses an async generator to generate
a sequence of random numbers.
It then uses an asynchronous
comprehension to iterate over
the async generator and collect the numbers in a list.

Example:
    async_comprehension() -> [0.123, 0.456, 0.789]

"""


import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Perform an asynchronous comprehension.

    Returns:
        A list of floats generated
        by the async generator.

    """
    res = [i async for i in async_generator()]
    return res
