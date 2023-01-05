import asyncio
import logging

from recipe_indexer.utils.argparse import parse_args


async def main():
    environment, verbose, config = await parse_args()

    logger = logging.getLogger()

    if verbose:
        logger.setLevel(logging.DEBUG)

    logger.debug(environment, config)

    # TODO: It may do some stuff


if __name__ == "__main__":
    asyncio.run(main())
