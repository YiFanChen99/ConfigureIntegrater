#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import collections


def deep_update(origin, prior):
    for key, value in prior.items():
        if isinstance(value, collections.Mapping):
            org = origin.get(key, {})
            if isinstance(org, collections.Mapping):
                origin[key] = deep_update(org, value)
            else:
                origin[key] = value
        else:
            origin[key] = value
    return origin


def get_matched_dir_path(path, project_dir_name):
    """
    Maybe useless, used before with mixed source-and-unit-test.
    """
    while True:
        head, tail = os.path.split(path)
        if tail == project_dir_name:
            return path
        elif head == path:
            raise ValueError(path)
        else:
            path = head
