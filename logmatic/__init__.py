import logging.handlers
from pythonjsonlogger import jsonlogger
import datetime
import socket


class JsonFormatter(jsonlogger.JsonFormatter):
    def __init__(self,
                 fmt="%(asctime) %(name) %(processName) %(filename)  %(funcName) %(levelname) %(lineno) %(module) %(threadName) %(message)",
                 datefmt="%Y-%m-%dT%H:%M:%S%z",
                 extra={}, *args, **kwargs):
        self._extra = extra
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, datefmt=datefmt, *args, **kwargs)

    def process_log_record(self, log_record):
        # Enforce the presence of a timestamp
        if "asctime" in log_record:
            log_record["timestamp"] = log_record["asctime"]
        else:
            log_record["timestamp"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        if self._extra is not None:
            for key, value in self._extra.items():
                log_record[key] = value
        return super(JsonFormatter, self).process_log_record(log_record)


# Derive from object to force a new-style class and thus allow super() to work
# on Python 2.6
class LogmaticHandler(logging.handlers.SocketHandler, object):
    """Python logging handler. Sends events over TCP.
    :param host: The host of the logstash server.
    :param port: The port of the logstash server (default 5959).
    """

    def __init__(self, logmaticKey, host="api.logmatic.io", port=10514):
        super(LogmaticHandler, self).__init__(host, port)
        self.logmaticKey = logmaticKey

    def makePickle(self, record):
        return self.logmaticKey.encode() + " ".encode() + self.formatter.format(record).encode() + "\n".encode()


# Allow SyslogHandler to emit in Json with a prefix (for instance appname)
class SysLogJsonHandler(logging.handlers.SysLogHandler):
    # Override constructor
    def __init__(self, address=('localhost', logging.handlers.SYSLOG_UDP_PORT),
                 facility=logging.handlers.SysLogHandler.LOG_USER, socktype=None, prefix=""):
        super(SysLogJsonHandler, self).__init__(address, facility, socktype)
        self._prefix = prefix
        if self._prefix != "":
            self._prefix = prefix + ": "

    # Override format method to handle prefix
    def format(self, record):
        return self._prefix + super(SysLogJsonHandler, self).format(record)
