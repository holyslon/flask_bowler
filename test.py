# -*- coding: utf-8 -*-

import unittest
from mock import MagicMock, patch

import flask
from flask.ext.bower import install


class InstallCommandTests(unittest.TestCase):

    def test_that_install_command_call_install_for_bower(self):
        mock = MagicMock(return_value=0)
        with patch('subprocess.call', mock) as call_mock:
            assert install("bootstrap") is True
            call_mock.assert_called_with([
                "bower",
                "install",
                "--save",
                "bootstrap"
            ], cwd="static")
