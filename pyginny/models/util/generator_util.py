import pkgutil

import pyginny.generators
from pyginny.models.logger import Logger


class GeneratorUtil(object):
    @staticmethod
    def get_all_generators_options():
        package = pyginny.generators

        prefix = package.__name__ + "."

        result = ""

        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            Logger.d("Found submodule {0} (is a package: {1})".format(modname, ispkg))
            module = __import__(modname + ".generator", fromlist=["dummy"])
            Logger.d("Imported {0}".format(module))

            obj = module.Generator(options=[], model=None)
            result = result + obj.get_usage_options()

        return result

    @staticmethod
    def run_all_generators(options, model):
        package = pyginny.generators

        prefix = package.__name__ + "."

        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            Logger.d("Found submodule {0} (is a package: {1})".format(modname, ispkg))
            module = __import__(modname + ".generator", fromlist=["dummy"])
            Logger.d("Imported {0}".format(module))

            obj = module.Generator(options=options, model=model)
            obj.run()
