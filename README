# logmatic-python
Python helpers to send logs to Logmatic.io.

It mainly contains a proper JSON formatter and a socket handler that streams logs directly to Logmatic.io - so no need to use a log shipper if you don't wan't to.

# Usage

## Use the JSON formatter

To use the JSON formatter, simply associate it to any handler such as the StreamHandler here.

```python
import logmatic-python

logger = logging.getLogger()

handler = logging.StreamHandler()
handler.setFormatter(logmatic.JsonFormatter(extra={"hostname":socket.gethostname()}))

logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

Once this setup is done, any child logger will use this configuration (eg `logging.getlogger("my_logger")`). As you can see, you can associate any extra information to the base formatter such as the hostname here or any environment variable you'll need depending of your usage.

```python
test_logger = logging.getLogger("test")
test_logger.info("classic message", extra={"special": "value", "run": 12})
```

Returns the following format:
```javascript
{
  "asctime": "2016-02-16T09:51:31Z",
  "name": "test", "processName": "MainProcess",
  "filename": "write_in_console.py",
  "funcName": "<module>",
  "levelname": "INFO",
  "lineno": 20,
  "module": "write_in_console",
  "threadName": "MainThread",
  "message": "classic message",
  "special": "value",
  "run": 12,
  "timestamp": "2016-02-16T09:51:31Z",
  "hostname": "<your_hostname>"
}
```

Extra values are also added at the log level if required.

An exception will be displayed as follow - which suppresses the multiline issue of Traceback :
```javascript
{
  "asctime": "2016-02-16T09:51:31Z",
  "name": "test", "processName": "MainProcess",
  "filename": "write_in_console.py",
  "funcName": "exception_test",
  "levelname": "ERROR",
  "lineno": 26,
  "module": "write_in_console",
  "threadName": "MainThread",
  "message": "This is a fake exception",
  "exc_info": "Traceback (most recent call last):\n  File \"test/write_in_console.py\", line 24, in exception_test\n    raise Exception('test')\nException: test",
  "timestamp": "2016-02-16T09:51:31Z",
  "hostname": "<your_hostname>"}
```

## Stream log straight to Logmatic.io

The LogmaticHandler can be coupled to the JsonFormatter as follow:

```python
import logmatic

logger = logging.getLogger()

handler = logmatic.LogmaticHandler("<your_api_key>")
handler.setFormatter(logmatic.JsonFormatter(extra={"hostname":socket.gethostname()}))

logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

Don't forget to replace <your_api_key> by the one provided on your Logmatic.io's platform.

With this configuration, any log coming from your Python's application will be sent to your platform and will fulfill the same format as described in the previous section.

Please contact us if you want anything more to be added in this toolset!
