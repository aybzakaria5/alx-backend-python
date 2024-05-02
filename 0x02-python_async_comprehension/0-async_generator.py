#!/user/bin/env python3
"""async_generator module"""
import asyncio
import random


async def async_generator():
    """async_generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
