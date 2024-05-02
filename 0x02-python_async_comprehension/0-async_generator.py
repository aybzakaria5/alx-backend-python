#!/usr/bin/env python3

"""
This module contains an async generator function called async_generator.

Keyword arguments:
None

Return:
None
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    Use the random module.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
