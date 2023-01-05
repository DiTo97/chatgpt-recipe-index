import asyncio
import typing


Gatherable = typing.Union[asyncio.Task, typing.Generator, typing.Coroutine]


def _gatherable_to_task(gatherable: Gatherable) -> asyncio.Task:
    """It converts a gatherable to 'asyncio.Task'"""
    if isinstance(gatherable, asyncio.Task):
        return gatherable

    return asyncio.create_task(gatherable)


async def gather(*args: Gatherable) -> tuple:
    """It wraps 'asyncio.gather' to cancel all tasks if any raise

    Raises
    ------
    Exception
        If any tasks raise
    """
    tasks = [_gatherable_to_task(arg) for arg in args]

    try:
        return await asyncio.gather(*tasks)
    except Exception as e:
        for t in tasks:
            t.cancel()

        raise e
