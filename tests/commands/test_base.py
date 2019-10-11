from unittest import TestCase

import pytest

from pyginny.commands import BaseCommand


class TestBase(TestCase):
    def test_run_error(self):
        with pytest.raises(NotImplementedError) as error:
            command = BaseCommand(None, None, None)
            command.run()

        self.assertEqual(error.type, NotImplementedError)
