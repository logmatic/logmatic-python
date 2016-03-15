```bash
[loggers]
keys=root, gunicorn.error, gunicorn.access

[handlers]
keys=json_syslog

[logger_root]
level=DEBUG
handlers=syslog

[logger_gunicorn.error]
level=ERROR
handlers=json_syslog
propagate=0
qualname=gunicorn.error

[logger_gunicorn.access]
level=DEBUG
handlers=json_syslog
propagate=0
qualname=gunicorn.access

[handler_json_syslog]
class=logmatic.SysLogJsonHandler
level=INFO
formatter = json
args=('/dev/log', handlers.SysLogHandler.LOG_LOCAL7, None ,"my_app")

[formatter_json]
format = %(asctime) %(name) %(processName) %(filename)  %(funcName) %(levelname) %(lineno) %(module) %(threadName) %(message)
class=logmatic.JsonFormatter

```
