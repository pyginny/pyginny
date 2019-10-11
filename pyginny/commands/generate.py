"""Generate command"""
import os
from os.path import join

from textx import metamodel_from_file

from pyginny.models.logger import Logger
from pyginny.models.util.file_util import FileUtil
from pyginny.models.util.generator_util import GeneratorUtil
from .base_command import BaseCommand


def get_meta_model():
    """
    Builds and returns a meta-model for Entity language.
    """
    entity_mm = metamodel_from_file(
        join(FileUtil.get_current_dir(), "extras", "dsl", "dsl.tx")
    )

    return entity_mm


class Generate(BaseCommand):
    def run(self):
        meta_model = get_meta_model()
        model = meta_model.model_from_file(os.path.expanduser(self.options["<file>"]))

        GeneratorUtil.run_all_generators(options=self.options, model=model)
        Logger.done()
