import logging
import time

import orjson
import structlog

structlog.configure(
    cache_logger_on_first_use=True,
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    processors=[
        structlog.threadlocal.merge_threadlocal_context,
        structlog.processors.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt="iso", utc=False),
        structlog.processors.JSONRenderer(serializer=orjson.dumps),
    ],
    logger_factory=structlog.BytesLoggerFactory(),
)


logger = structlog.stdlib.get_logger()

log = logger.bind()

log.info("Hello world!")
time.sleep(1)
log.info("This is a log entry")
time.sleep(1)
log.info("Here's another", some_data=3)
time.sleep(1)
log.info("I don't know what else to put here, honestly", foo="bar", baz={"spam": "ham"})
time.sleep(1)
log.info("Latest line entry. Goodbye for now!")
