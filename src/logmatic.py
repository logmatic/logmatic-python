
from logging.handlers import SocketHandler
from pythonjsonlogger import jsonlogger
import datetime
import socket

class JsonFormatter(jsonlogger.JsonFormatter):
    def __init__(self,
            fmt = "%(asctime) %(name) %(processName) %(filename)  %(funcName) %(levelname) %(lineno) %(module) %(threadName) %(message)",
            datefmt = "%Y-%m-%dT%H:%M:%SZ",
            extra = {},*args):
        self._extra = extra
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt,datefmt=datefmt,*args)

    def process_log_record(self, log_record):
        # Enforce the presence of a timestamp
        if "asctime" in log_record:
            log_record["timestamp"] = log_record["asctime"]
        else:
            log_record["timestamp"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        if self._extra is not None:
            for key, value in self._extra.iteritems():
                log_record[key] = value
        return super(JsonFormatter, self).process_log_record(log_record)

# Derive from object to force a new-style class and thus allow super() to work
# on Python 2.6
class LogmaticHandler(SocketHandler, object):
    """Python logging handler for Logstash. Sends events over TCP.
    :param host: The host of the logstash server.
    :param port: The port of the logstash server (default 5959).
    :param message_type: The type of the message (default logstash).
    :param fqdn; Indicates whether to show fully qualified domain name or not (default False).
    :param version: version of logstash event schema (default is 0).
    :param tags: list of tags for a logger (default is None).
    """

    def __init__(self, logmaticKey,host="api.logmatic.io", port=10514):
        super(LogmaticHandler, self).__init__(host, port)
        self.logmaticKey = logmaticKey

    def makePickle(self, record):
        return self.logmaticKey + " " + self.formatter.format(record) + b'\n'
