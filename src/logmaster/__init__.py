"""
Logmaster
~~~~~~~~~

A simple logging module for Python.

Usage
-----

    >>> from logmaster import Logger
    >>> logger = Logger('logs.log')
    >>> logger.log('info', 'This is an info message.', 'additional info')
    >>> logger.log('warning', 'This is a warning message.', 'additional info')
    >>> logger.log('error', 'This is an error message.', 'additional info')
    >>> logger.log('critical', 'This is a critical message.', 'additional info')
    >>> logger.log('debug', 'This is a debug message.', 'additional info')
    >>> logger.log('success', 'This is a success message.', 'additional info')
    >>> logger.log('fail', 'This is a fail message.', 'additional info')
    >>> logger.log('custom', 'This is a custom message.', 'additional info')

:license: MIT, see LICENSE for more details.
:copyright: W1L7dev (c) 2023-present.
"""

__title__ = 'logmaster'
__version__ = '0.1.0'
__author__ = 'W1L7dev'
__license__ = 'MIT'


from .logger import *