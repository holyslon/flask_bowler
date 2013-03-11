# -*- coding: utf-8 -*-

import unittest
from mock import Mock

import flask
from flask.ext.bower import register_commands, Install


class EqualToAnyObjectOfType:

    def __init__(self, target_type):
        self.target_type = target_type

    def __eq__(self, other):
        return self.target_type == type(other)

    def __ne__(self, other):
        return self.target_type != type(other)


def has_type(target_type):
    return EqualToAnyObjectOfType(target_type)


class RegisterCommandTest(unittest.TestCase):

    def setUp(self):
        self.manager = Mock()

    def test_that_install_command_is_registred(self):
        register_commands(self.manager)

        self.manager.add_command.assert_called_with('install', has_type(Install))

