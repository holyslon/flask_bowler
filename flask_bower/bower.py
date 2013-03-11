# -*- coding: utf-8 -*-
from subprocess import call


class BowerCall:

    def __init__(self, base_folder):
        self.base_folder = base_folder

    def call_and_return_status(self, args):
        call_result = call(["bower"].append(args), cwd=self.base_folder)
        return True if call_result == 0 else False


class Bower:

    def __init__(self, caller):
        self.caller = caller

    def install(self, package, save=True):
        return self.caller.call_and_return_status([
            "install",
            "--save" if save else "",
            package
        ])
