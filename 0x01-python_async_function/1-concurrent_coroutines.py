#!/usr/bin/env python3
"""
     an asynchronous coroutine
     that takes in an integer argument
     (max_delay, with a default value of 10)
    """

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values).
in ascending order without using sort() because of concurrency.
    """
    sorted_tasks = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = asyncio.as_completed(tasks)
    for task in completed:
        result = await task
        sorted_tasks.append(result)
    return sorted_tasks # list of delay of tasks sorte as completed
