############################################################
# -*- coding: utf-8 -*-
#
# SAAS log and messaging system
#
# Francisco José Calvo Fernández (http://www.irydeo.com)
# (c) 2021
# Licence GPL v3
############################################################

from PyQt5.QtCore import pyqtSignal, QObject

class Logger(QObject):
    log_signal = pyqtSignal(str)

    def send_message(self, msg):
        # emit signal
        print("Emit signal: " + msg)
        self.log_signal.emit(msg)


