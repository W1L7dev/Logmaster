import datetime
from typing import Optional

class Colors:
    def __init__(self):
        self.green = '\033[92m'
        self.red = '\033[31m'
        self.yellow = '\033[33m'
        self.blue = '\033[34m'
        self.magenta = '\033[35m'
        self.cyan = '\033[96m'
        self.reset = '\033[0m'


class Logger(Colors):
    def __init__(self, filename: Optional[str] = None):
        super().__init__()
        self.filename = filename

    def log(self, level: str, message: str, additional_info: Optional[str] = None):
        if level == "info":
            output = f"{self.green}[{datetime.datetime.now()}] [INFO] {message}"
        elif level == "warning":
            output = f"{self.yellow}[{datetime.datetime.now()}] [WARNING] {message}"
        elif level == "error":
            output = f"{self.red}[{datetime.datetime.now()}] [ERROR] {message}"
        elif level == "critical":
            output = f"{self.magenta}[{datetime.datetime.now()}] [CRITICAL] {message}"
        elif level == "debug":
            output = f"{self.blue}[{datetime.datetime.now()}] [DEBUG] {message}"
        elif level == "success":
            output = f"{self.cyan}[{datetime.datetime.now()}] [SUCCESS] {message}"
        elif level == "fail":
            output = f"{self.red}[{datetime.datetime.now()}] [FAIL] {message}"
        elif level == "custom":
            output = f"{self.yellow}[{datetime.datetime.now()}] [CUSTOM] {message}"

        if additional_info:
            output += f" | {additional_info}"
        print(output + self.reset)
        if self.filename:
            with open(self.filename, "a+") as f:
                f.write(output + "\n")
        return output + self.reset