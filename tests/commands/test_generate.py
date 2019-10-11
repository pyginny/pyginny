import os
from subprocess import PIPE, Popen as popen
from unittest import TestCase

from pyginny.models.constants import Constants
from pyginny.models.util.file_util import FileUtil


class TestGenerate(TestCase):
    def test_generate(self):
        filename = "records.{0}".format(Constants.EXTENSION)
        file_path = os.path.join(
            FileUtil.get_current_dir(), "extras", "examples", filename
        )

        params = ["pyginny", "generate", file_path]
        output = popen(params, stdout=PIPE, stderr=PIPE).communicate()[0]
        output = str(output)
        print(output)

        required = "[DONE]"

        self.assertIn(required, output)

    def test_generate_without_params(self):
        params = ["pyginny", "generate"]
        output = popen(params, stdout=PIPE, stderr=PIPE).communicate()[1]
        output = str(output)
        print(output)

        required = "Usage"

        self.assertIn(required, output)

    def test_generate_with_invalid_params(self):
        params = ["pyginny", "generate", "--my-param", "my-value"]
        output = popen(params, stdout=PIPE, stderr=PIPE).communicate()[1]
        output = str(output)
        print(output)

        required = "Usage"

        self.assertIn(required, output)
