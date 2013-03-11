# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import with_statement

from flask.ext.script import Manager
from subprocess import call

__all__ = ["install"]


manager = Manager()


@manager.command
def install(package):
    call_result = call([
        "bower",
        "install",
        "--save",
        package
    ], cwd="source")
    return True if call_result else False
