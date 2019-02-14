#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

from ..Loader import ConfigureLoader as Loader


DIR_PATH_TEST = os.getcwd() + os.sep + "ConfigureIntegrator" + os.sep + "Test"
FILE_MISSED = "Missed.json"


class LoadFileTest(unittest.TestCase):
    def assertLoad(self, expected, filename, dir_path=DIR_PATH_TEST):
        self.assertEqual(expected, Loader.load_file(dir_path, filename))

    def test_file_exist(self):
        expected = {'obj': {"1": 1, "2": 2}}
        self.assertLoad(expected, "ConfigDefault.json")

        expected = {'obj': {"1": 3, "3": 3}}
        self.assertLoad(expected, "ConfigUser.json")

    def test_file_not_exist(self):
        self.assertLoad({}, FILE_MISSED)

    def test_dir_path_end_with_and_without_separator(self):
        expected = {'obj': {"1": 1, "2": 2}}

        # without_separator
        dir_path = DIR_PATH_TEST
        self.assertLoad(expected, "ConfigDefault.json", dir_path=dir_path)

        # with_separator
        dir_path += os.sep
        self.assertLoad(expected, "ConfigDefault.json", dir_path=dir_path)

        # with more than one separators
        dir_path += os.sep
        self.assertLoad(expected, "ConfigDefault.json", dir_path=dir_path)


class LoadIntegratedConfigTest(unittest.TestCase):
    def assertLoad(self, expected, **kwargs):
        actual = Loader.load_integrated_config(DIR_PATH_TEST, **kwargs)
        self.assertEqual(expected, actual)

    def test_default_filename(self):
        expected = {'obj': {"1": 3, "2": 2, "3": 3}}
        self.assertLoad(expected)
        self.assertLoad(expected, default_file=None, user_file=None)
        self.assertLoad(expected, default_file=Loader.CONFIG_FILENAME_DEFAULT,
                        user_file=Loader.CONFIG_FILENAME_USER)

    def test_given_filename(self):
        expected = {'obj': {"1": 1, "3": 3, "2": 2}}
        self.assertLoad(expected, default_file=Loader.CONFIG_FILENAME_USER,
                        user_file=Loader.CONFIG_FILENAME_DEFAULT)

        expected = {'obj': {"1": 3, "3": 3}}
        self.assertLoad(expected, default_file=FILE_MISSED, user_file=Loader.CONFIG_FILENAME_USER)
        self.assertLoad(expected, default_file=Loader.CONFIG_FILENAME_USER, user_file=FILE_MISSED)
