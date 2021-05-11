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
import time

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from ui.main_ui import Ui_MainWindow
from Director import Director
from Profile import Profile
from Options import Options
import threading

from PyQt5.QtCore import QObject, QThread, pyqtSignal


class Saas(Ui_MainWindow):
    
    ##################
    ## Init function
    ##################
    def __init__(self, dialog):

        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.dialog = dialog
        self.is_dual_mode_enabled = True
        self.seq_thread = None
        self.update_ui_thread = None
        self.profiles = Profile()
        self.director = Director()
        self.options = Options()

        # Load profiles
        self.master_profile.addItems(self.profiles.get_list())
        self.slave_profile.addItems(self.profiles.get_list())

        # Set correct option
        self.object_name.setText(self.options.get("object_name", "Object name"))
        self.ar.setText(self.options.get("ar", "Enter AR hh:mm:ss"))
        self.dec.setText(self.options.get("dec", "Enter DEC dd:mm:ss"))
        self.master_profile.setCurrentText(self.options.get("master_profile", "None"))
        self.slave_profile.setCurrentText(self.options.get("slave_profile", "None"))
        self.master_port.setText(self.options.get("master_port", 3277))
        self.slave_port.setText(self.options.get("slave_port", 9999))
        self.integration_time.setValue(int(self.options.get("integration_time", 300)))
        self.master_bin.setValue(int(self.options.get("master_bin", 1)))
        self.slave_bin.setValue(int(self.options.get("slave_bin", 1)))
        self.master_single_exposure.setValue(int(self.options.get("master_single_exposure", 120)))
        self.slave_single_exposure.setValue(int(self.options.get("slave_single_exposure", 5)))
        self.dither_every.setValue(int(self.options.get("dither_every", 30)))

        self.is_dual_mode_enabled = bool(self.options.get("dual_mode", True))
        self.actionDual_mode.setChecked(self.is_dual_mode_enabled)

        self.sm_group_every.setValue(self.options.get("sm_group_every", 1))
        self.sm_group_delay.setValue(self.options.get("sm_group_delay", 1))
        self.sm_group_keyword.setText(self.options.get("sm_group_keyword", "GROUP"))
        if not self.is_dual_mode_enabled:
            self.slaveSystem.setDisabled(True)
            self.sm_burst_options.setEnabled(True)
            self.director.set_dual_mode(False)

        # Set initial parameters for Director
        self.set_params()

        # Connect menus
        self.actionDual_mode.changed.connect(self.dual_mode)

        # Connect input widgets
        self.master_bin.valueChanged.connect(self.set_params)
        self.slave_bin.valueChanged.connect(self.set_params)
        self.master_single_exposure.valueChanged.connect(self.set_params)
        self.slave_single_exposure.valueChanged.connect(self.set_params)
        self.dither_every.valueChanged.connect(self.set_params)
        self.integration_time.valueChanged.connect(self.set_params)
        self.object_name.editingFinished.connect(self.set_params)
        self.ar.editingFinished.connect(self.set_params)
        self.dec.editingFinished.connect(self.set_params)
        self.sm_group_every.valueChanged.connect(self.set_params)
        self.sm_group_delay.valueChanged.connect(self.set_params)
        self.sm_group_keyword.editingFinished.connect(self.set_params)

        # Connect start
        self.start.clicked.connect(self.start_click)

        # Connect stop
        self.stop.clicked.connect(self.stop_click)
        self.stop.setDisabled(bool(1))

        self.log.setText("Master status: " + str(self.director.current_master_exposures) + " of " + str(self.director.master_number_of_exposures))

    ##################
    ## Connect menu actions: Dual mode settings
    ##################
    def dual_mode(self):
        # Get current status
        if self.actionDual_mode.isChecked():   # Dual mode is enabled
            self.slaveSystem.setDisabled(False)
            self.options.set("dual_mode", True)
            self.sm_burst_options.setEnabled(False)
            self.director.set_dual_mode(True)
        else:                                   # Single mode
            self.slaveSystem.setDisabled(True)
            self.options.set("dual_mode", False)
            self.sm_burst_options.setEnabled(True)
            self.director.set_dual_mode(False)

    def load_latest_image(self, node):
        image = QImage()
        if node=="master":
            url_image = 'http://' + str(self.director.master_host) + ':' + str(self.director.master_port) +'/fullimage.jpg'
            image.loadFromData(requests.get(url_image).content)
            self.master_image.setPixmap(QPixmap(image.scaled(300, 250, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        else:
            url_image = 'http://' + str(self.director.slave_host) + ':' + str(
                self.director.slave_port) + '/fullimage.jpg'
            image.loadFromData(requests.get(url_image).content)
            self.slave_image.setPixmap(QPixmap(image.scaled(300, 250, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))

        self.master_image.show()



    ##################
    ## Let's go
    ##################
    def start_click(self):
        self.director.set_node("master", self.master_host.text(), self.master_port.text())
        self.director.set_integration_time(int(self.integration_time.value()))  # Set total integration time in seconds
        self.director.set_single_exposure_time("master", int(self.master_single_exposure.value()))  # Master exposures are 120s
        self.director.set_binning("master", int(self.master_bin.value()))
        self.director.set_frame_type("Light")

        if self.is_dual_mode_enabled:
            self.director.set_node("slave", self.slave_host.text(), self.slave_port.text())
            self.director.set_single_exposure_time("slave",
                                                   int(self.slave_single_exposure.value()))  # Master exposures are 120s
            self.director.set_binning("slave", int(self.slave_bin.value()))
        else:
            # Sigle mode
            self.director.set_sm_group_every(self.sm_group_every.value())
            self.director.set_sm_group_delay(self.sm_group_delay.value())

        self.director.set_dither_per_exposures(int(self.dither_every.value()))  # Dither each frame in master node, system will calculate needed data for slave

        # Rest of exposure data:
        self.director.set_object_name(self.object_name.text())  # it will be master_myObject and slave_myObject

        self.director.slew(self.ar.text(), self.dec.text())
        # self.director.sync()
        self.director.autofocus("master")

        if self.is_dual_mode_enabled:
            self.director.autofocus("slave")

        #self.director.start_guiding()

        self.seq_thread = threading.Thread(target= self.director.start_seq)
        self.seq_thread.start()

        self.update_ui_thread = threading.Thread(target=self.update_ui)
        self.update_ui_thread.start()
        #self.director.start_seq()  # It will launch each node, stop when needed...

        self.start.setDisabled(bool(1))
        self.stop.setEnabled(bool(1))



    def stop_click(self):
        # Send signals to terminate
        self.start.setEnabled(bool(1))
        self.stop.setDisabled(bool(1))
        print("")


    ##################
    ## Master profile is changed
    ##################
    def master_profile_changed(self):
        try:
            if self.master_profile.currentText() != self.slave_profile.currentText():
                port = self.profiles.get_port(self.master_profile.currentText())
                self.master_port.setText(str(port))
                self.options.set("master_profile", self.master_profile.currentText())
                self.options.set("master_port", port)
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
                self.options.set("slave_profile", self.slave_profile.currentText())
                self.options.set("slave_port", port)
            else:
                quit_msg = "Select a different profile. Master and slave can't be the same"
                reply = QMessageBox.information(self.dialog, 'Message',
                                                quit_msg, QMessageBox.Ok)
                self.slave_profile.clearEditText()
        except Exception as e:
            print(str(e))
            quit_msg = "Selected profile was created with an old CCDCiel version, please update it."
            reply = QMessageBox.information(self.dialog, 'Message',
                                         quit_msg, QMessageBox.Ok)

    def set_params(self):

        # Profile change
        self.master_profile.currentIndexChanged.connect(self.master_profile_changed)
        self.slave_profile.currentIndexChanged.connect(self.slave_profile_changed)

        # Set director parameters
        self.director.set_integration_time(self.integration_time.value())
        self.director.set_binning("master", int(self.master_bin.value()))
        self.director.set_binning("slave", int(self.slave_bin.value()))
        self.director.set_single_exposure_time("master", int(self.master_single_exposure.value()))
        self.director.set_single_exposure_time("slave", int(self.slave_single_exposure.value()))
        self.director.set_dither_per_exposures(int(self.dither_every.value()))

        self.options.set("object_name", self.object_name.text())
        self.options.set("ar", self.ar.text())
        self.options.set("dec", self.dec.text())

        self.options.set("integration_time", self.integration_time.value())
        self.options.set("master_bin", self.master_bin.value())
        self.options.set("slave_bin", self.slave_bin.value())
        self.options.set("master_single_exposure", self.master_single_exposure.value())
        self.options.set("slave_single_exposure", self.slave_single_exposure.value())
        self.options.set("dither_every", self.dither_every.value())

        # Single mode
        if not self.is_dual_mode_enabled:
            self.options.set("dual_mode", False)
            self.options.set("sm_group_every", self.sm_group_every.value())
            self.options.set("sm_group_delay", self.sm_group_delay.value())
            self.options.set("sm_group_keyword", self.sm_group_keyword.text())
            self.director.set_dual_mode(False)
            self.director.set_sm_group_every(self.sm_group_every.value())
            self.director.set_sm_group_delay(self.sm_group_delay.value())
            self.director.set_sm_group_keyword(self.sm_group_keyword.text())
        else: # Dual mode
            self.director.set_dual_mode(True)
            self.options.set("dual_mode", True)

        # Update class
        self.director.calculate_params()

        # Update UI
        self.log.setText("Master status: " + str(self.director.current_master_exposures) + " of " + str(
            self.director.master_number_of_exposures))

    def update_ui(self):
        # Update UI
        while(1):
            print("Calling update")
            self.log.setText("Master status: " + str(self.director.current_master_exposures) + " of " + str(
                self.director.master_number_of_exposures))
            self.load_latest_image("master")

            if self.is_dual_mode_enabled:
                self.load_latest_image("slave")

            time.sleep(int(self.director.master_single_exposure_time))


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
