import os
from unittest import TestCase

import pytest
from testfixtures import tempdir

from pyginny.models.util.file_util import FileUtil


class TestFileUtil(TestCase):
    @pytest.fixture(scope="class", autouse=True)
    def in_tmpdir(self, tmpdir_factory):
        d = tmpdir_factory.mktemp("d")
        with d.as_cwd():
            yield d

    @tempdir()
    def test_create_dir(self, d):
        os.chdir(d.path)

        dir_name_1 = "new-dir-1"
        dir_name_2 = "new-dir-2"

        FileUtil.create_dir(dir_name_1)
        FileUtil.create_dir(os.path.join(dir_name_1, dir_name_2))

        self.assertTrue(os.path.isdir(dir_name_1))
        self.assertTrue(os.path.isdir(os.path.join(dir_name_1, dir_name_2)))

    @tempdir()
    def test_remove_dir(self, d):
        os.chdir(d.path)

        dir_name_1 = "new-dir-1"
        dir_name_2 = "new-dir-2"

        FileUtil.create_dir(dir_name_1)
        FileUtil.create_dir(os.path.join(dir_name_1, dir_name_2))
        FileUtil.remove_dir(dir_name_1)

        self.assertFalse(os.path.isdir(dir_name_1))
        self.assertFalse(os.path.isdir(os.path.join(dir_name_1, dir_name_2)))

    @tempdir()
    def test_remove_file(self, d):
        os.chdir(d.path)

        filename = "new-file.txt"

        FileUtil.write_to_file(".", filename, "content test")

        self.assertTrue(os.path.isfile(filename))

        FileUtil.remove_file(filename)

        self.assertFalse(os.path.isfile(filename))

    @tempdir()
    def test_write_to_file(self, d):
        os.chdir(d.path)

        filename = "new-file.txt"

        FileUtil.write_to_file(".", filename, "content test")

        self.assertTrue(os.path.isfile(filename))
        self.assertEqual(os.path.getsize(filename), 12)

    @tempdir()
    def test_find_files(self, d):
        os.chdir(d.path)

        FileUtil.write_to_file(".", "file1.txt", "")
        FileUtil.write_to_file(".", "file2.txt", "")
        FileUtil.write_to_file(".", "file3.log", "")

        files_txt = FileUtil.find_files("file*.txt")
        files_log = FileUtil.find_files("file*.log")

        self.assertEqual(len(files_txt), 2)
        self.assertEqual(len(files_log), 1)

    def test_normalize_path(self):
        normalized = FileUtil.normalize_path("C:\\pyginny\\Test")
        expected = "C:/pyginny/Test"

        self.assertEqual(normalized, expected)

    def test_normalize_path_from_list(self):
        paths = ["C:\\pyginny\\Test1", "C:\\pyginny\\Test2"]
        normalized = FileUtil.normalize_path_from_list(paths)
        expected1 = "C:/pyginny/Test1"
        expected2 = "C:/pyginny/Test2"

        self.assertEqual(normalized[0], expected1)
        self.assertEqual(normalized[1], expected2)
