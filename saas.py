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
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from ui.main_ui import Ui_MainWindow
from ui.master_advanced_options import Ui_MasterAdvancedOptions
from ui.slave_advanced_options import Ui_SlaveAdvancedOptions
from ui.saas_options_ui import Ui_SaaSOptions
from saas_options import SaasOptions
from object_selector import ObjectSelector
from director import Director
from profile import Profile
from options import Options
from logger import Logger
import threading

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
        self.options = Options()

        # Logger and Director
        self.logger = Logger()
        self.logger.log_signal.connect(self.update_from_signal)
        self.director = Director(self.logger)

        # Load profiles
        self.master_profile.addItems(self.profiles.get_list())
        self.slave_profile.addItems(self.profiles.get_list())


        # Set correct option
        self.object_name.setText(self.options.get("object_name", "Object name"))
        self.ar.setText(self.options.get("ar", "Enter AR hh:mm:ss"))
        self.dec.setText(self.options.get("dec", "Enter DEC dd:mm:ss"))
        self.master_profile.setCurrentText(self.options.get("master_profile", "None"))
        self.slave_profile.setCurrentText(self.options.get("slave_profile", "None"))
        #self.master_port.setText(self.options.get("master_port", 3277))
        #self.slave_port.setText(self.options.get("slave_port", 9999))
        self.integration_time.setValue(int(self.options.get("integration_time", 300)))
        self.master_bin.setValue(int(self.options.get("master_bin", 1)))
        self.slave_bin.setValue(int(self.options.get("slave_bin", 1)))
        self.master_single_exposure.setValue(int(self.options.get("master_single_exposure", 120)))
        self.slave_single_exposure.setValue(int(self.options.get("slave_single_exposure", 5)))
        self.dither_every.setValue(int(self.options.get("dither_every", 30)))

        self.is_dual_mode_enabled = bool(self.options.get("dual_mode", True))
        self.actionDual_mode.setChecked(self.is_dual_mode_enabled)

        if not self.is_dual_mode_enabled:
            self.slaveSystem.setDisabled(True)
            #self.sm_burst_options.setEnabled(True)
            self.director.set_dual_mode(False)
            self.statusbar.showMessage("Single mode")
        else:
            self.statusbar.showMessage("Dual mode")

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

        # Master basic controls (Slew / Sync / Focus)
        self.master_slew.clicked.connect(self.slew_telescope)
        self.master_sync.clicked.connect(self.sync_telescope)
        self.master_focus.clicked.connect(self.focus_master_telescope)

        # Dialogs
        self.master_adv_options.clicked.connect(self.show_master_adv_options)
        self.slave_adv_options.clicked.connect(self.show_slave_adv_options)
        self.actionSequence_options.triggered.connect(self.show_sequence_adv_options)
        self.actionExit.triggered.connect(self.close_app)
        self.actionAbout_SaaS.triggered.connect(self.show_about_saas)
        self.open_object_selector.clicked.connect(self.show_object_selector)

        # Connect start
        self.start.clicked.connect(self.start_click)

        # Connect stop
        self.stop.clicked.connect(self.stop_click)
        self.stop.setDisabled(bool(1))

        # TODO: delete and replace by new signal/slot systems
        self.log.setText("Master status: " + str(self.director.current_master_exposures) + " of " + str(self.director.master_number_of_exposures))

    ##################
    ## Slew telescope to given coords
    ##################
    def slew_telescope(self):
        self.director.set_node("master", self.options.get("master_host", "localhost"),
                               self.options.get("master_port", "3277"))
        self.director.slew(self.ar.text(), self.dec.text())

    ##################
    ## Solve and sync mount
    ##################
    def sync_telescope(self):
        self.director.set_node("master", self.options.get("master_host", "localhost"),
                               self.options.get("master_port", "3277"))
        self.director.sync()

    ##################
    ## Autofocus master telescope
    ##################
    def focus_master_telescope(self):
        self.director.set_node("master", self.options.get("master_host", "localhost"),
                                   self.options.get("master_port", "3277"))
        self.director.autofocus("master")

    ##################
    ## Master advanced options
    ##################
    def show_master_adv_options(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_MasterAdvancedOptions()
        dialog.ui.setupUi(dialog)
        dialog.ui.sm_group_every.setValue(int(self.options.get("sm_group_every", 1)))
        dialog.ui.sm_group_delay.setValue(self.options.get("sm_group_delay", 1))
        dialog.ui.sm_group_keyword.setText(self.options.get("sm_group_keyword", "GROUP"))
        dialog.ui.master_host.setText(self.options.get("master_host", "localhost"))
        dialog.ui.master_port.setText(self.options.get("master_port", "3277"))
        r = dialog.exec_()
        dialog.show()
        if r:
            print("OK, saving...")
            self.options.set("sm_group_every", dialog.ui.sm_group_every.value())
            self.options.set("sm_group_keyword", dialog.ui.sm_group_keyword.text())
            self.options.set("master_host", dialog.ui.master_host.text())
            self.options.set("master_port", dialog.ui.master_port.text())
            self.options.set("sm_group_delay", dialog.ui.sm_group_delay.value())
            self.config_director()
        else:
            print("Cancel")

    ##################
    ## Master advanced options
    ##################
    def show_slave_adv_options(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_SlaveAdvancedOptions()
        dialog.ui.setupUi(dialog)
        dialog.ui.slave_host.setText(self.options.get("slave_host", "localhost"))
        dialog.ui.slave_port.setText(self.options.get("slave_port", "3278"))
        r = dialog.exec_()
        dialog.show()
        if r:
            print("OK, saving...")
            self.options.set("slave_host", dialog.ui.slave_host.text())
            self.options.set("slave_port", dialog.ui.slave_port.text())
            self.config_director()
        else:
            print("Cancel")

    ##################
    ## Sequence options
    ##################
    def show_sequence_adv_options(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = SaasOptions(dialog, self.options)
        r = dialog.exec_()
        # TODO: Save options
        if r:
            print("Saving")
            dialog.ui.save_options()
        else:
            print("Cancel")

    ##################
    ## Object manager and selector
    ##################
    def show_object_selector(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = ObjectSelector(dialog, self.options)
        r = dialog.exec_()

        # TODO: Save options
        if r:
            print("OK")
            self.object_name.setText(self.options.get("object_name", "0"))
            self.ar.setText(self.options.get("ar", "0"))
            self.dec.setText(self.options.get("dec", "0"))
            self.master_single_exposure.setValue(self.options.get("master_single_exposure", "0"))
            self.slave_single_exposure.setValue(self.options.get("slave_single_exposure", "0"))
            print("VALUE " + str(self.options.get("slave_single_exposure", "0")))
        else:
            print("Cancel")

    ##################
    ## About SaaS
    ##################
    def show_about_saas(self):
        QMessageBox.about(self.dialog, "SaaS", "Scientific Astronomy Automation Software pre-Alpha")

    ##################
    ## Exit SaaS
    ##################
    def close_app(self):
        quit_msg = "Are you sure?"
        reply = QMessageBox.question(self.dialog, 'Close SaaS',
                                     quit_msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            app.quit()

    ##################
    ## Receiving a signal to update UI from rest of the system
    ##################
    def update_from_signal(self, msg):
        # Update UI
        self.log_signal.setText(msg)
        # TODO: Master/slave diferentiation
        print("Signal received " + msg)

    ##################
    ## Connect menu actions: Dual mode settings
    ##################
    def dual_mode(self):
        # Get current status
        if self.actionDual_mode.isChecked():   # Dual mode is enabled
            self.slaveSystem.setDisabled(False)
            self.options.set("dual_mode", True)
            #self.sm_burst_options.setEnabled(False)
            self.director.set_dual_mode(True)
            self.logger.send_message("LOG")
            self.statusbar.showMessage("Dual mode")
        else:                                   # Single mode
            self.slaveSystem.setDisabled(True)
            self.options.set("dual_mode", False)
            #self.sm_burst_options.setEnabled(True)
            self.director.set_dual_mode(False)
            self.statusbar.showMessage("Single mode")

    ##################
    ## Load latest captured image in each node
    ##################
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
        try:
            # TODO: Read from config and not from UI directly
            #-- self.director.set_node("master", self.master_host.text(), self.master_port.text())
            self.director.set_node("master", self.options.get("master_host", "localhost"), self.options.get("master_port", "3277"))

            self.director.set_integration_time(int(self.integration_time.value()))  # Set total integration time in seconds
            self.director.set_single_exposure_time("master", int(self.master_single_exposure.value()))  # Master exposures are 120s
            self.director.set_binning("master", int(self.master_bin.value()))
            self.director.set_frame_type("Light")

            if self.is_dual_mode_enabled:
                self.director.set_node("slave", self.options.get("slave_host", "localhost"), self.options.get("slave_port", "3278"))
                self.director.set_single_exposure_time("slave",
                                                       int(self.slave_single_exposure.value()))  # Master exposures are 120s
                self.director.set_binning("slave", int(self.slave_bin.value()))
            else:
                # Sigle mode
                self.director.set_sm_group_every(self.options.get("sm_group_every", 10))
                self.director.set_sm_group_delay(self.options.get("sm_group_delay", 10))
                self.director.set_sm_group_keyword(self.options.get("sm_group_keyword", 10))

            self.director.set_dither_per_exposures(int(self.dither_every.value()))  # Dither each frame in master node, system will calculate needed data for slave

            # Rest of exposure data:
            self.director.set_object_name(self.object_name.text())  # it will be master_myObject and slave_myObject

            if self.options.get("op_slew", False):
                self.director.slew(self.ar.text(), self.dec.text())
                self.director.sync()

            if self.options.get("op_focus", False):
                self.director.autofocus("master")

            if self.is_dual_mode_enabled:
                self.director.autofocus("slave")

            if self.options.get("op_guiding", False):
                self.director.start_guiding()

            self.seq_thread = threading.Thread(target= self.director.start_seq)
            self.seq_thread.start()

            self.update_ui_thread = threading.Thread(target=self.update_ui)
            self.update_ui_thread.start()
            #self.director.start_seq()  # It will launch each node, stop when needed...

            self.start.setDisabled(bool(1))
            self.stop.setEnabled(bool(1))
        except Exception as e:
            print(str(e))
            msg = "Error starting sequence: " + str(e)
            reply = QMessageBox.information(self.dialog, 'Message',
                                         msg, QMessageBox.Ok)

    ##################
    ## Stop current sequence (To-Do)
    ##################
    def stop_click(self):
        # Send signals to terminate
        self.start.setEnabled(bool(1))
        self.stop.setDisabled(bool(1))


    ##################
    ## Master profile is changed
    ##################
    def master_profile_changed(self):
        # TODO: Read from config and not from UI directly
        try:
            if self.master_profile.currentText() != self.slave_profile.currentText():
                port = self.profiles.get_port(self.master_profile.currentText())
                self.master_port.setText(str(port))
                self.options.set("master_profile", self.master_profile.currentText())
                self.options.set("master_port", port)

                # Read all options, but it should be also readed at start!!

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

    ##################
    ## Save selected parameters
    ##################
    def save_config(self):
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
        else:  # Dual mode
            self.options.set("dual_mode", True)

    ##################
    ## Lets configure our sequence director
    ##################
    def config_director(self):
        # Profile change
        self.master_profile.currentIndexChanged.connect(self.master_profile_changed)
        self.slave_profile.currentIndexChanged.connect(self.slave_profile_changed)

        # Set director parameters
        self.director.set_integration_time(self.options.get("integration_time", 1))
        self.director.set_binning("master", int(self.options.get("master_bin", 1)))
        self.director.set_binning("slave", int(self.options.get("slave_bin", 1)))
        self.director.set_single_exposure_time("master", int(self.options.get("master_single_exposure", 10)))
        self.director.set_single_exposure_time("slave", int(self.options.get("slave_single_exposure", 10)))
        self.director.set_dither_per_exposures(int(self.options.get("dither_every", 30)))

        # Single mode
        if not self.is_dual_mode_enabled:
            self.director.set_dual_mode(False)
            self.director.set_sm_group_every(self.options.get("sm_group_every", 10))
            self.director.set_sm_group_delay(self.options.get("sm_group_delay", 10))
            self.director.set_sm_group_keyword(self.options.get("sm_group_keyword", 10))
            self.statusbar.showMessage("Single mode")
        else:  # Dual mode
            self.director.set_dual_mode(True)
            self.statusbar.showMessage("Dual mode")

        # Update class
        self.director.calculate_params()


    ##################
    ## Live change / save selected parameters
    ##################
    def set_params(self):
        self.save_config()
        self.config_director()
        # Update UI
        self.log.setText("Master status: " + str(self.director.current_master_exposures) + " of " + str(
            self.director.master_number_of_exposures))


    ##################
    ## System to update UI (to be replaced by a signal/slots system)
    ##################
    def update_ui(self):
        # TODO: Replace by signal/slots
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
