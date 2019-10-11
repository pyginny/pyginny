"""Base generator"""

from pyginny.models.logger import Logger
from pyginny.models.util.file_util import FileUtil


class BaseGenerator(object):
    def __init__(self, options, model):
        self.options = options
        self.model = model

    def get_name(self):
        raise NotImplementedError("You must implement the get_name() method yourself!")

    def get_usage_options(self):
        raise NotImplementedError(
            "You must implement the get_usage_options() method yourself!"
        )

    def run(self):
        if not self.can_run():
            Logger.i("Generator '{0}' skipped".format(self.get_name()))
            return

        # create the output folder
        output_path = self.get_output_path()
        FileUtil.prepare_output_path(output_path)

        # process all records found
        self.process_record_list()

        # finished
        Logger.s("Generator '{0}' finished".format(self.get_name()))

    def get_output_path(self):
        raise NotImplementedError(
            "You must implement the get_output_path() method yourself!"
        )

    def process_record_list(self):
        raise NotImplementedError(
            "You must implement the process_record_list() method yourself!"
        )

    def can_run(self):
        raise NotImplementedError("You must implement the can_run() method yourself!")

    def get_nl(self):
        return "\n"

    def get_indent(self):
        return "    "

    def get_option(self, name):
        if name in self.options:
            return self.options[name]

        return ""
