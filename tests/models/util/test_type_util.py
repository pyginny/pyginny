from unittest import TestCase

from pyginny.models.util.generator_util import GeneratorUtil
from pyginny.models.util.type_util import TypeUtil


class TestTypeUtil(TestCase):
    def test_simple_value(self):
        value = None
        self.assertTrue(TypeUtil.is_empty(value))

    def test_string_value(self):
        value = ""
        self.assertTrue(TypeUtil.is_empty(value))

    def test_not_empty_value(self):
        value = 123
        self.assertFalse(TypeUtil.is_empty(value))

    def test_not_empty_string_value(self):
        value = "123"
        self.assertFalse(TypeUtil.is_empty(value))
