# Logmaster
## A simple logging package for


---

### Installation
```bash
pip install logmaster
```
> note: this package is not yet on PyPI, so you will have to install it from source.
> Depending on your python installation, the command mayt vary. For example, if you are using python3, you may need to use `pip3` instead of `pip`.

### Usage
```python
from logmaster import Logger

logger = Logger("my_log_file.log")

logger.log("info", "Hello, world!")
```

### Documentation
#### Logger
##### `Logger(path: str)`
Creates a new logger object. The path argument is the path to the log file. If the file does not exist, it will be created. If it does exist, it will be appended to.

##### `Logger.log(level: str, message: str, additional_info: Optional[str])`
Logs a message to the log file. The level argument is the level of the message. The message argument is the message to log. The additional_info argument is optional, and is used to provide additional information about the message.




