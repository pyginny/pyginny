from subprocess import PIPE, Popen as popen
from unittest import TestCase

from pyginny import __version__ as VERSION


class TestCLI(TestCase):
    def test_returns_usage_information(self):
        output = popen(["pyginny", "-h"], stdout=PIPE).communicate()[0]
        output = str(output)
        print(output)

        self.assertTrue("Usage" in output)

        output = popen(["pyginny", "--help"], stdout=PIPE).communicate()[0]
        output = str(output)
        print(output)

        self.assertTrue("Usage:" in output)

    def test_returns_version_information(self):
        output = popen(["pyginny", "--version"], stdout=PIPE).communicate()[0]
        output = str(output)
        print(output)

        self.assertTrue(VERSION in output)

    def test_debug(self):
        output = popen(["pyginny", "-d"], stdout=PIPE).communicate()[0]
        output = str(output)
        print(output)

        self.assertTrue("System information" in output)
        self.assertTrue("You supplied the following options" in output)
