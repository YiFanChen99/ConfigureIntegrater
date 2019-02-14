#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from ..Utility import *


class DeepUpdateTest(unittest.TestCase):
    def test_level_1(self):
        origin = {'1': 3, 'r': '66', 4: 9}
        prior = {'1': 4, '4': 2}

        expected = {'1': 4, 'r': '66', 4: 9, '4': 2}
        self.assertEqual(expected, deep_update(origin, prior))

    def test_deep_level(self):
        origin = {
            3: {
                2: {
                    1: {2: '3212'}
                },
                4: 4
            },
            4: {
                1: {1: '411'}
            }
        }
        prior = {
            3: {
                2: {
                    1: {6: '3216'}
                },
                4: 6
            },
            4: {
                1: {2: '412'}
            }
        }

        expected = {
            3: {
                2: {
                    1: {
                        2: '3212',
                        6: '3216'
                    }
                },
                4: 6
            },
            4: {
                1: {
                    1: '411',
                    2: '412'
                },
            }
        }
        self.assertEqual(expected, deep_update(origin, prior))

    def test_update_dict_and_primitive(self):
        origin = {'o': {3: 3}, 'p': 1}
        prior = {'o': 4, 'p': {5: 5}}

        expected = {'o': 4, 'p': {5: 5}}
        self.assertEqual(expected, deep_update(origin, prior))


class GetMatchedDirPathTest(unittest.TestCase):
    PROJECT_DIR = "ConfigureIntegrator"
    EXPECTED = "D:\\Projects\\ConfigureIntegrator"

    def assertGetDir(self, path, project=None):
        if project is None:
            project = self.PROJECT_DIR

        self.assertEqual(self.EXPECTED, get_matched_dir_path(path, project))

    def test_path_included(self):
        self.assertGetDir(self.EXPECTED)
        self.assertGetDir(self.EXPECTED + "\\SubDir1\\File")

    def test_invalid_path(self):
        with self.assertRaises(ValueError):
            self.assertGetDir("")

        with self.assertRaises(ValueError):
            self.assertGetDir(self.EXPECTED[:-1])

    def test_different_project_dir(self):
        self.assertGetDir(self.EXPECTED, self.PROJECT_DIR)

        with self.assertRaises(ValueError):
            self.assertGetDir(self.EXPECTED, "AAA")
