############################################################
# -*- coding: utf-8 -*-
#
# SAAS main file
#
# Francisco José Calvo Fernández (http://www.irydeo.com)
# (c) 2021
# Licence GPL v3
############################################################

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.main_ui import Ui_MainWindow
from Director import Director
from Profile import Profile


class Saas(Ui_MainWindow):
    
    ##################
    ## Init function
    ##################
    def __init__(self, dialog):

        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.dialog = dialog
        self.profiles = Profile()
        self.director = Director()

        self.master_profile.addItems(self.profiles.get_list())
        self.slave_profile.addItems(self.profiles.get_list())
        self.start.clicked.connect(self.start_click)
        self.master_profile.currentIndexChanged.connect(self.master_profile_changed)
        self.slave_profile.currentIndexChanged.connect(self.slave_profile_changed)

    ##################
    ## Let's go
    ##################
    def start_click(self):
        self.director.set_node("master", self.master_host.text(), self.master_port.text())
        self.director.set_node("slave", self.slave_host.text(), self.slave_port.text())
        self.director.set_integration_time(int(self.integration_time.value()))  # Set total integration time in seconds
        self.director.set_single_exposure_time("master", int(self.master_single_exposure.value()))  # Master exposures are 120s
        self.director.set_single_exposure_time("slave", int(self.slave_single_exposure.value()))  # Master exposures are 120s
        self.director.set_binning("master", int(self.master_bin.value()))
        self.director.set_binning("slave", int(self.slave_bin.value()))
        self.director.set_frame_type("Light")

        self.director.set_dither_per_exposures(int(self.dither_every.value()))  # Dither each frame in master node, system will calculate needed data for slave

        # Rest of exposure data:
        self.director.set_object_name(self.object_name.text())  # it will be master_myObject and slave_myObject

        self.director.slew(self.ar.text(), self.dec.text())
        # self.director.sync()
        self.director.autofocus("master")
        self.director.autofocus("slave")
        self.director.start_guiding()
        self.director.start_seq()  # It will launch each node, stop when needed...

    ##################
    ## Master profile is changed
    ##################
    def master_profile_changed(self):
        try:
            if self.master_profile.currentText() != self.slave_profile.currentText():
                port = self.profiles.get_port(self.master_profile.currentText())
                self.master_port.setText(str(port))
            else:
                quit_msg = "Select a different profile. Master and slave can be the same"
                reply = QMessageBox.information(self.dialog, 'Message',
                                                quit_msg, QMessageBox.Ok)
                self.master_profile.setCurrentText("")
        except Exception as e:
            print(str(e))
            quit_msg = "Selected profile was created with an old CCDCiel version, please update it."
            reply = QMessageBox.information(self.dialog, 'Message',
                                         quit_msg, QMessageBox.Ok)

    ##################
    ## Slave profile is changed
    ##################
    def slave_profile_changed(self):
        try:
            if self.master_profile.currentText() != self.slave_profile.currentText():
                port = self.profiles.get_port(self.slave_profile.currentText())
                self.slave_port.setText(str(port))
            else:
                quit_msg = "Select a different profile. Master and slave can be the same"
                reply = QMessageBox.information(self.dialog, 'Message',
                                                quit_msg, QMessageBox.Ok)
                self.slave_profile.setCurrentText("")
        except Exception as e:
            print(str(e))
            quit_msg = "Selected profile was created with an old CCDCiel version, please update it."
            reply = QMessageBox.information(self.dialog, 'Message',
                                         quit_msg, QMessageBox.Ok)

##################
## Entry point
##################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #dialog = QtWidgets.QDialog()
    dialog = QtWidgets.QMainWindow()
    prog = Saas(dialog)
    dialog.show()
    sys.exit(app.exec_())
