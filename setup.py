"""Packaging settings."""

import os
from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from pyginny import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""

    description = "run tests"
    user_options = [("codecoverage=", None, "With code coverage")]

    def initialize_options(self):
        self.codecoverage = None

    def finalize_options(self):
        assert self.codecoverage in (None, "html")

    def run(self):
        """Run all tests!"""
        options = ["py.test"]

        if self.codecoverage == "html":
            html_path = "{0}".format(os.path.join(os.getcwd(), "htmlcov"))
            options += [
                "--cov=pyginny",
                "--cov-report=term-missing",
                "--cov-report=html:" + html_path,
            ]

        errno = call(options)
        raise SystemExit(errno)


setup(
    name="pyginny",
    version=__version__,
    description="pyginny cli tool.",
    long_description=long_description,
    url="https://github.com/pyginny/pyginny",
    author="Paulo Coutinho",
    author_email="paulo@prsolucoes.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: Public Domain",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="cli",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=[
        "pyyaml==5.4",
        "docopt==0.6.2",
        "python-slugify==3.0.4",
        "colorama==0.4.1",
    ],
    extras_require={"test": ["coverage", "pytest", "pytest-cov", "testfixtures"]},
    entry_points={"console_scripts": ["pyginny=pyginny.cli:main"]},
    cmdclass={"test": RunTests},
)
