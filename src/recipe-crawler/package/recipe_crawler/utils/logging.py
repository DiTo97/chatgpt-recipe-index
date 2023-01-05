import asyncio
import logging
import logging.handlers

try:
    # Python 3.7 and newer
    from queue import SimpleQueue as Queue
except ImportError:
    from queue import Queue


class LocalQueueHandler(logging.handlers.QueueHandler):
    """A class that adds cancellation handling to 'logging.QueueHandler'"""
    def emit(self, record: logging.LogRecord) -> None:
        try:
            self.enqueue(record)
        except asyncio.CancelledError:
            raise
        except Exception:
            self.handleError(record)


def init_logging_queue() -> None:
    """
    It replaces the handlers of the Python root logger with a 'LocalQueueHandler'.
    By doing so, we are able to defer them to a separate thread avoiding blocking I/O
    with a 'logging.QueueListener' holding the original handlers.

    It also sets the formatting of the Python root logger.
    """
    logger = logging.getLogger()  # The Python root logger

    O_handlers = logger.handlers  # Original handlers

    # FIXME: How to prevent duplicate logs?
    if any(isinstance(h, LocalQueueHandler) for h in O_handlers):
        return

    queue = Queue()

    formatter = logging.Formatter(
        "%(asctime)s [%(process)d] %(levelname)-5s [%(name)-48s] %(message)s"
    )

    handler = LocalQueueHandler(queue)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    N_handlers = []  # New handlers

    for h in O_handlers:
        if h is not handler:
            logger.removeHandler(h)
            N_handlers.append(h)

    listener = logging.handlers.QueueListener(
        queue, *N_handlers, respect_handler_level=True
    )

    listener.start()
