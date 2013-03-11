# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import with_statement

from .install import Install

__all__ = ["Install", "register_commands"]


def register_commands(manager):
    manager.add_command('install', Install())
