#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from .Utility import deep_update
from .JsonAccessor.JsonAccessor import load_json


class ConfigureLoader(object):
    CONFIG_FILENAME_DEFAULT = "ConfigDefault.json"
    CONFIG_FILENAME_USER = "ConfigUser.json"

    @staticmethod
    def load_file(dir_path, filename):
        if dir_path[-1] != os.sep:
            dir_path += os.sep

        try:
            return load_json(dir_path + filename)
        except FileNotFoundError:
            return {}

    @classmethod
    def load_integrated_config(cls, dir_path, default_file=None, user_file=None):
        """
        Loading both default and user config, return the integrated result.
        """
        if default_file is None:
            default_file = cls.CONFIG_FILENAME_DEFAULT
        if user_file is None:
            user_file = cls.CONFIG_FILENAME_USER

        default_config = cls.load_file(dir_path, default_file)
        user_config = cls.load_file(dir_path, user_file)
        return deep_update(default_config, user_config)
