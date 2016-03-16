# Gunicorn integration

## Send to syslog

`SysLogJsonHandler` is designed to correctly send events to syslog in Json (RFC-5424 norm). With this handler,
you can add a prefix in order to set the correct application name.

```
Mar 15 16:49:00 my_hostname my_app: {"process": 1815, "levelname": "WARNING", "name": "app.server", "message": "Could not load environment configuration, falling back to default", "timestamp": "2016-03-15T16:49:00.005720Z"}
```

Edit your log configuration file as follow.

```properties
[loggers]
keys=root

[handlers]
keys=json_syslog

[logger_root]
level=DEBUG
handlers=json_syslog

[handler_json_syslog]
class=logmatic.SysLogJsonHandler
level=INFO
formatter = json
args=('/dev/log', handlers.SysLogHandler.LOG_LOCAL7, None ,"my_app")

[formatter_json]
class=logmatic.JsonFormatter
```

Eventually you can complete the log record with others fields. Refer to the official [Python documentation](https://docs.python.org/2/library/logging.html#logrecord-attributes)

## Sent to Logmatic.io

Gunicorn is able to directly log to Logmatic.io. Edit your log configuration file as follow.
```properties
[loggers]
keys=root

[handlers]
keys=logmatic

[logger_root]
level=DEBUG
handlers=logmatic

[handler_logmatic]
class=logmatic.LogmaticHandler
formatter=json
args=("<your_api_key>","api.logmatic.io",10514)

[formatter_json]
class=logmatic.JsonFormatter
```