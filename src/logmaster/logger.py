import datetime
from typing import Optional

import os
from .errors import *


class Colors:
    def __init__(self):
        self.colors_levels = {
            "success": "\033[92m",
            "fail": "\033[31m",
            "warning": "\033[33m",
            "info": "\033[34m",
            "critical": "\033[35m",
            "debug": "\033[96m",
            "error": "\033[0m",
        }
        self.reset = "\033[0m"
        self.bold = "\033[1m"


class Logger(Colors):
    def __init__(self, filename: Optional[str] = None) -> None:
        super().__init__()
        self.filename = filename
        self.levels = [
            "info",
            "warning",
            "error",
            "critical",
            "debug",
            "success",
            "fail",
        ]

    def log(
        self,
        level: str,
        message: str,
        additional_info: Optional[str] = None,
        show_datetime: Optional[bool] = True,
        show_filename: Optional[bool] = True,
        show_type: Optional[bool] = True,
    ):
        output = ""
        if level not in self.levels:
            raise InvalidLevel(f"Invalid level: {level}")

        self.color = self.colors_levels[level]

        if show_datetime:
            output += f"{self.color}[{datetime.datetime.now()}] "
        if show_filename:
            output += f"{self.color}[{os.path.basename(__file__)}] "
        if show_type:
            output += f"{self.color}[{level.upper()}] "

        output += f"{self.color}{self.bold}{message}{self.reset}"
        if additional_info:
            output += f"{self.color}[{additional_info}]{self.reset}"
        if self.filename:
            with open(self.filename, "a") as f:
                f.write(output + "\n")
        print(output)

Logger().log(level="info", message="This is an info message.", additional_info="additional info")