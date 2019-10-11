from unittest import TestCase

from pyginny.models.constants import Constants


class TestConstants(TestCase):
    def test_initial_data(self):
        self.assertEqual(Constants.DEBUG, False)
        self.assertEqual(Constants.EXTENSION, "ginny")
        self.assertEqual(Constants.BUILD_DIR, "build")
        self.assertEqual(Constants.ENV_VAR_PREFIX, "PYGINNY_")
