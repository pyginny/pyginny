from unittest import TestCase

from pyginny.models.util.generator_util import GeneratorUtil


class TestGeneratorUtil(TestCase):
    def test_generators_options(self):
        output = GeneratorUtil.get_all_generators_options()
        required = "Generator Java"

        self.assertIn(required, output)

    def test_generators_run(self):
        GeneratorUtil.run_all_generators({}, None)

        self.assertTrue(True)
