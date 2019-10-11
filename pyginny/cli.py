"""
pyginny

Usage:
  pyginny generate <file> [options] [-d | --debug]
  pyginny -h | --help
  pyginny -d | --debug

Options:
  -h --help            Show this screen.
  -d --debug           Enable debug messages.
  --version            Show version.

{0}

Examples:
  pyginny generate my-project.ginny

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/pyginny/pyginny
"""
import os
import platform
from inspect import getmembers, isclass
from json import dumps

from colorama import init as colorama_init
from docopt import docopt

import pyginny.commands
from pyginny.models.constants import Constants
from pyginny.models.logger import Logger
from pyginny.models.util.generator_util import GeneratorUtil
from . import __version__


def main():
    """Main CLI entrypoint."""
    colorama_init()

    generators_options = GeneratorUtil.get_all_generators_options()

    commands_doc = __doc__
    commands_doc = commands_doc.format(generators_options)

    options = docopt(commands_doc, version=__version__)

    # show all params for debug
    if ("--debug" in options and options["--debug"]) or (
        "-d" in options and options["-d"]
    ):
        Constants.DEBUG = True

        Logger.clean("System information: ")
        Logger.clean("> PROCESS ID : {0}".format(os.getpid()))
        Logger.clean("> PYTHON     : {0}".format(platform.python_version()))
        Logger.clean("")
        Logger.clean("You supplied the following options: ")
        Logger.clean("{0}".format(dumps(options, indent=2, sort_keys=False)))
        Logger.clean("")

    # dynamically match the command that user is trying to run
    for (option_key, option_value) in options.items():
        if hasattr(pyginny.commands, option_key) and option_value:
            command_module = getattr(pyginny.commands, option_key)
            commands = getmembers(command_module, isclass)

            found_command = None

            for command in commands:
                if command[0] != "Base" and command[0].lower() == option_key:
                    found_command = command[1](options)
                    break

            if found_command:
                found_command.run()
