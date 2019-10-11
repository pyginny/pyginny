import sys

from colorama import Fore, Style

from pyginny.models.constants import Constants


class Logger(object):
    @staticmethod
    def e(msg, fatal=True):
        """
        Print error message and exit with error code 10
        unless 'fatal' is False.
        :param msg:   string message
        :param fatal: exit program with error code 10 if True (default is true)
        """
        print("{0}[ERROR]{1} {2}".format(Fore.RED, Style.RESET_ALL, msg))

        if fatal:
            sys.exit(1)

    @staticmethod
    def w(msg):
        """
        Print a warning message
        :param msg: string message
        """
        print("{0}[WARNING]{1} {2}".format(Fore.YELLOW, Style.RESET_ALL, msg))

    @staticmethod
    def ok(msg=""):
        """
        Print a green 'ok' message
        :param msg: string message
        """
        print("{0}[OK]{1} {2}".format(Fore.GREEN, Style.RESET_ALL, msg))

    @staticmethod
    def done(msg=""):
        """
        Print a green 'done' message
        :param msg: string message
        """
        print("{0}[DONE]{1} {2}".format(Fore.GREEN, Style.RESET_ALL, msg))

    @staticmethod
    def s(msg=""):
        """
        Print a green 'ok' message
        :param msg: string message
        """
        print("{0}[SUCCESS]{1} {2}".format(Fore.GREEN, Style.RESET_ALL, msg))

    @staticmethod
    def f(msg="", fatal=True):
        """
        Print a red 'fail' message
        :param msg: string message
        :param fatal: stop execution
        """
        print("{0}[FAIL]{1} {2}".format(Fore.RED, Style.RESET_ALL, msg))

        if fatal:
            sys.exit(1)

    @staticmethod
    def i(msg):
        """
        Print a yellow 'info' message
        :param msg: string message
        """
        print("{0}[INFO]{1} {2}".format(Fore.CYAN, Style.RESET_ALL, msg))

    @staticmethod
    def d(msg):
        """
        Print a white 'debug' message
        :param msg: string message
        """
        if Constants.DEBUG:
            print("{0}[DEBUG]{1} {2}".format(Fore.WHITE, Style.RESET_ALL, msg))

    @staticmethod
    def clean(msg):
        """
        Print a normal log message
        :param msg: string message
        """
        print(msg)

    @staticmethod
    def colored(msg, color):
        """
        Print a colored log message
        :param msg:   text message
        :param color: color escape sequence (e.g. log.YELLOW)
        """
        print("{0}{1}{2}".format(color, msg, Style.RESET_ALL))
