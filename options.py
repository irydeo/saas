############################################################
# -*- coding: utf-8 -*-
#
# SAAS save & load options
#
# Francisco José Calvo Fernández (http://www.irydeo.com)
# (c) 2021
# Licence GPL v3
############################################################

from easysettings import EasySettings


class Options:
    def __init__(self):
        self.settings = EasySettings("saas.conf")

    def set(self, key, value):
        if key == "slave_single_exposure":
            print("Setting: " + str(value))
        self.settings.setsave(key, value)

    def get(self, key, default=""):
        return self.settings.get(key, default)
