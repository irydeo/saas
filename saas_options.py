############################################################
# -*- coding: utf-8 -*-
#
# SAAS main file
#
# Francisco José Calvo Fernández (http://www.irydeo.com)
# (c) 2021
# Licence GPL v3
############################################################
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from ui.master_advanced_options import Ui_MasterAdvancedOptions
from ui.saas_options_ui import Ui_SaaSOptions
from profile import Profile
from ui.slave_advanced_options import Ui_SlaveAdvancedOptions


class SaasOptions(Ui_SaaSOptions):

    ##################
    ## Init function
    ##################
    def __init__(self, dialog, options):
        Ui_SaaSOptions.__init__(self)
        self.master_port = 0
        self.setupUi(dialog)
        self.dialog = dialog
        self.options = options
        self.profiles = Profile()

        # Load profiles
        self.master_profile.addItems(self.profiles.get_list())
        self.slave_profile.addItems(self.profiles.get_list())

        # Load options
        self.load_options()

        # Profile change
        self.master_profile.currentIndexChanged.connect(self.master_profile_changed)
        self.slave_profile.currentIndexChanged.connect(self.slave_profile_changed)

        # Connections
        self.refresh.clicked.connect(self.refresh_from_profiles)
        self.master_adv_options.clicked.connect(self.show_master_adv_options)
        self.slave_adv_options.clicked.connect(self.show_slave_adv_options)

    def refresh_from_profiles(self):
        self.op_master_fl.setValue(float(self.profiles.get_focal_lenght(self.master_profile.currentText())))
        self.op_master_pixel_size.setValue(float(self.profiles.get_pixel_size(self.master_profile.currentText())))
        self.op_slave_fl.setValue(float(self.profiles.get_focal_lenght(self.slave_profile.currentText())))
        self.op_slave_pixel_size.setValue(float(self.profiles.get_pixel_size(self.slave_profile.currentText())))


    ##################
    ## Master profile is changed
    ##################
    def master_profile_changed(self):
        # TODO: Read from config and not from UI directly
        try:
            if self.master_profile.currentText() != self.slave_profile.currentText():
                port = self.profiles.get_port(self.master_profile.currentText())
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

    def save_options(self):
        self.options.set("op_master_fl", self.op_master_fl.value())
        self.options.set("op_slave_fl", self.op_slave_fl.value())
        self.options.set("op_master_pixel_size", self.op_master_pixel_size.value())
        self.options.set("op_slave_pixel_size", self.op_slave_pixel_size.value())

        self.options.set("op_focus", self.op_focus.isChecked())
        self.options.set("op_autofocus_master", self.op_autofocus_master.isChecked())
        self.options.set("op_autofocus_slave", self.op_autofocus_slave.isChecked())
        self.options.set("op_slew", self.op_slew.isChecked())
        self.options.set("op_guiding", self.op_guiding.isChecked())
        self.options.set("op_use_autoguiding_master", self.op_use_autoguiding_master.isChecked())
        self.options.set("op_use_autoguiding_slave", self.op_use_autoguiding_slave.isChecked())
        self.options.set("op_dithering", self.op_dithering.isChecked())
        self.options.set("op_autoconnect", self.op_autoconnect.isChecked())
        self.options.set("op_warm", self.op_warm.isChecked())
        self.options.set("op_close_shutter", self.op_close_shutter.isChecked())
        self.options.set("op_calibrate_at_the_end", self.op_calibrate_at_the_end.isChecked())
        self.options.set("op_calibrate_use_filter", self.op_calibrate_use_filter.isChecked())
        self.options.set("op_calibrate_close_shutter", self.op_calibrate_close_shutter.isChecked())

        self.options.set("master_profile", self.master_profile.currentText())
        port = self.profiles.get_port(self.master_profile.currentText())
        self.options.set("master_port", port)

        self.options.set("slave_profile", self.slave_profile.currentText())
        port = self.profiles.get_port(self.slave_profile.currentText())
        self.options.set("slave_port", port)

    def load_options(self):
        self.op_master_fl.setValue(int(self.options.get("op_master_fl", 800)))
        self.op_slave_fl.setValue(int(self.options.get("op_slave_fl", 800)))
        self.op_master_pixel_size.setValue(float(self.options.get("op_master_pixel_size", 800)))
        self.op_slave_pixel_size.setValue(float(self.options.get("op_slave_pixel_size", 800)))


        self.op_focus.setChecked(self.options.get("op_focus", False))
        self.op_autofocus_master.setChecked(self.options.get("op_autofocus_master", False))
        self.op_autofocus_slave.setChecked(self.options.get("op_autofocus_slave", False))
        self.op_slew.setChecked(self.options.get("op_slew", False))
        self.op_guiding.setChecked(self.options.get("op_guiding", False))
        self.op_use_autoguiding_master.setChecked(self.options.get("op_use_autoguiding_master", False))
        self.op_use_autoguiding_slave.setChecked(self.options.get("op_use_autoguiding_slave", False))
        self.op_dithering.setChecked(self.options.get("op_dithering", False))
        self.op_autoconnect.setChecked(self.options.get("op_autoconnect", False))
        self.op_warm.setChecked(self.options.get("op_warm", False))
        self.op_close_shutter.setChecked(self.options.get("op_close_shutter", False))
        self.op_calibrate_at_the_end.setChecked(self.options.get("op_calibrate_at_the_end", False))
        self.op_calibrate_use_filter.setChecked(self.options.get("op_calibrate_use_filter", False))
        self.op_calibrate_close_shutter.setChecked(self.options.get("op_calibrate_close_shutter", False))

        self.master_profile.setCurrentText(self.options.get("master_profile", ""))
        self.slave_profile.setCurrentText(self.options.get("slave_profile", ""))

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
        else:
            print("Cancel")