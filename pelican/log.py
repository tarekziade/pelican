import os
import sys
from logging import CRITICAL, ERROR,  WARN, INFO, DEBUG
from logging import critical, error, info, warning, warn, debug
from logging import Formatter, getLogger, StreamHandler

global ANSI
ANSI = {
    'gray' : lambda(text) : u'\033[1;30m' + unicode(text) + u'\033[0;m',
    'red' : lambda(text) : u'\033[1;31m' + unicode(text) + u'\033[0;m',
    'green' : lambda(text) : u'\033[1;32m' + unicode(text) + u'\033[0;m',
    'yellow' : lambda(text) : u'\033[1;33m' + unicode(text) + u'\033[0;m',
    'blue' : lambda(text) : u'\033[1;34m' + unicode(text) + u'\033[0;m',
    'magenta' : lambda(text) : u'\033[1;35m' + unicode(text) + u'\033[0;m',
    'cyan' : lambda(text) : u'\033[1;36m' + unicode(text) + u'\033[0;m',
    'white' : lambda(text) : u'\033[1;37m' + unicode(text) + u'\033[0;m',
    'bgred' : lambda(text) : u'\033[1;41m' + unicode(text) + u'\033[0;m',
    'bggreen' : lambda(text) : u'\033[1;42m' + unicode(text) + u'\033[0;m',
    'bgbrown' : lambda(text) : u'\033[1;43m' + unicode(text) + u'\033[0;m',
    'bgblue' : lambda(text) : u'\033[1;44m' + unicode(text) + u'\033[0;m',
    'bgmagenta' : lambda(text) : u'\033[1;45m' + unicode(text) + u'\033[0;m',
    'bgcyan' : lambda(text) : u'\033[1;46m' + unicode(text) + u'\033[0;m',
    'bggray' : lambda(text) : u'\033[1;47m' + unicode(text) + u'\033[0;m',
    'bgyellow' : lambda(text) : u'\033[1;43m' + unicode(text) + u'\033[0;m',
    'bggrey' : lambda(text) : u'\033[1;100m' + unicode(text) + u'\033[0;m'
}


class ANSIFormatter(Formatter):
    """
    Convert a `logging.LogReport' object into colored text, using ANSI escape sequences.
    """
    ## colors:

    def format(self, record):
        if record.levelname is 'INFO':
            return ANSI['cyan']('-> ') + unicode(record.msg)
        elif record.levelname is 'WARNING':
            return ANSI['yellow'](record.levelname) + ': ' + unicode(record.msg)
        elif record.levelname is 'ERROR':
            return ANSI['red'](record.levelname) + ': ' + unicode(record.msg)
        elif record.levelname is 'CRITICAL':
            return ANSI['bgred'](record.levelname) + ': ' + unicode(record.msg)
        elif record.levelname is 'DEBUG':
            return ANSI['bggrey'](record.levelname) + ': ' + unicode(record.msg)
        else:
            return ANSI['white'](record.levelname) + ': ' + unicode(record.msg)


class TextFormatter(Formatter):
    """
    Convert a `logging.LogReport' object into text.
    """

    def format(self, record):
        if not record.levelname or record.levelname is 'INFO':
            return record.msg
        else:
            return record.levelname + ': ' + record.msg


class DummyFormatter(object):
    """
    A dummy class.
    Return an instance of the appropriate formatter (ANSIFormatter if
    sys.stdout.isatty() is True, else TextFormatter)
    """

    def __new__(cls, *args, **kwargs):
        if os.isatty(sys.stdout.fileno())\
           and not sys.platform.startswith('win'):
            return ANSIFormatter(*args, **kwargs)
        else:
            return TextFormatter( *args, **kwargs)


def init(level=None, logger=getLogger(), handler=StreamHandler()):
    fmt = DummyFormatter()
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    if level:
        logger.setLevel(level)


if __name__ == '__main__':
    init(level=DEBUG)
    debug('debug')
    info('info')
    warning('warning')
    error('error')
    critical('critical')


__all__ = [
    "debug",
    "info",
    "warn",
    "warning",
    "error",
    "critical",
    "DEBUG",
    "INFO",
    "WARN",
    "ERROR",
    "CRITICAL"
]
