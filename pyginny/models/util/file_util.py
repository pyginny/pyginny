import fnmatch
import glob
import os
import shutil
import subprocess
from subprocess import PIPE

from pyginny.models.logger import Logger


class FileUtil(object):
    @staticmethod
    def create_dir(dir_path):
        Logger.d("Create a new dir: {0}".format(dir_path))

        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

    @staticmethod
    def remove_dir(dir_path):
        Logger.d("Remove dir: {0}".format(dir_path))

        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

    @staticmethod
    def remove_file(filename):
        Logger.d("Remove file: {0}".format(filename))

        if os.path.isfile(filename):
            os.remove(filename)

    @staticmethod
    def write_to_file(dir_path, filename, content):
        Logger.d(
            "Creating file {0} in directory {1} with {2} bytes...".format(
                filename, dir_path, len(content)
            )
        )

        full_file_path = os.path.join(dir_path, filename)
        FileUtil.remove_file(full_file_path)
        FileUtil.create_dir(dir_path)

        with open(full_file_path, "w") as f:
            f.write(content)
            f.close()

        Logger.d("Created file {0} in directory {1}".format(filename, dir_path))

    @staticmethod
    def read_file(file_path):
        Logger.d("Reading file: {0}".format(file_path))

        with open(file_path, "r") as f:
            content = f.read()
            f.close()

        return content

    @staticmethod
    def get_current_dir():
        return FileUtil.normalize_path(os.getcwd())

    @staticmethod
    def run(args, cwd, env):
        proc = subprocess.Popen(args, env=env, cwd=cwd, stdout=PIPE, stderr=PIPE)

        out, err = proc.communicate()
        exitcode = proc.returncode

        return exitcode, err, out

    @staticmethod
    def copy_files_from_list(copy_file_list):
        if copy_file_list:
            for copy_file_item in copy_file_list:
                FileUtil.copy_file(
                    from_path=copy_file_item["from"], to_path=copy_file_item["to"]
                )

    @staticmethod
    def copy_file(from_path, to_path):
        FileUtil.create_dir(os.path.dirname(from_path))
        FileUtil.create_dir(os.path.dirname(to_path))

        shutil.copyfile(from_path, to_path)

    @staticmethod
    def find_files(from_path):
        files = []

        for f in glob.glob(from_path):
            files.append(f)

        return files

    @staticmethod
    def normalize_path(path):
        if path:
            path = path.replace("\\", "/")
            return path
        else:
            ""

    @staticmethod
    def normalize_path_from_list(paths):
        if paths:
            new_path_list = []

            for path in paths:
                new_path_list.append(FileUtil.normalize_path(path))

            return new_path_list
        else:
            return []

    @staticmethod
    def find_dirs(from_path, pattern):
        results = []
        for root, dirs, _ in os.walk(from_path, topdown=False):
            for name in dirs:
                path = os.path.join(root, name)
                dirname = os.path.basename(path)

                if fnmatch.fnmatch(dirname, pattern):
                    results.append(path)

        return results

    @staticmethod
    def find_dirs_simple(from_path, pattern):
        results = []
        for item in os.listdir(from_path):
            path = os.path.join(from_path, item)

            if os.path.isdir(path):
                if fnmatch.fnmatch(item, pattern):
                    results.append(path)

        return results

    @staticmethod
    def prepare_output_path(output_path):
        output_dir = os.path.expanduser(output_path)

        if not os.path.exists(output_dir):
            FileUtil.create_dir(output_dir)
