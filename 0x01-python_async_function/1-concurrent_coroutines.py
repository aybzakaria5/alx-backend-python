#!/usr/bin/env python3
"""docs for task 1"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """docs for task 1"""
    sorted_tasks = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = asyncio.as_completed(tasks)
    for task in completed:
        result = await task
        sorted_tasks.append(result)
    return sorted_tasks
