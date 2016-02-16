import logging
import sys
import datetime
import socket
from pythonjsonlogger import jsonlogger

sys.path.append('src/')
import logmatic

logger = logging.getLogger()

handler = logging.StreamHandler()
handler.setFormatter(logmatic.LogmaticFormatter(extra={"hello": "world","hostname":socket.gethostname()}))

logger.addHandler(handler)
logger.setLevel(logging.INFO)

test_logger = logging.getLogger("test")
test_logger.info({"special": "value", "run": 12})
test_logger.info("classic message", extra={"special": "value", "run": 12})

def exception_test():
    try:
        raise Exception('test')
    except Exception:
        test_logger.exception("This is a fake exception")

exception_test()
