# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saas_options_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaaSOptions(object):
    def setupUi(self, SaaSOptions):
        SaaSOptions.setObjectName("SaaSOptions")
        SaaSOptions.resize(558, 540)
        self.buttonBox = QtWidgets.QDialogButtonBox(SaaSOptions)
        self.buttonBox.setGeometry(QtCore.QRect(210, 500, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(SaaSOptions)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 541, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.devices = QtWidgets.QWidget()
        self.devices.setObjectName("devices")
        self.op_master_fl = QtWidgets.QSpinBox(self.devices)
        self.op_master_fl.setGeometry(QtCore.QRect(140, 46, 81, 22))
        self.op_master_fl.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.op_master_fl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.op_master_fl.setMinimum(1)
        self.op_master_fl.setMaximum(10000)
        self.op_master_fl.setSingleStep(100)
        self.op_master_fl.setProperty("value", 800)
        self.op_master_fl.setObjectName("op_master_fl")
        self.label_163 = QtWidgets.QLabel(self.devices)
        self.label_163.setGeometry(QtCore.QRect(10, 8, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_163.setFont(font)
        self.label_163.setObjectName("label_163")
        self.label_39 = QtWidgets.QLabel(self.devices)
        self.label_39.setGeometry(QtCore.QRect(10, 78, 121, 21))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.devices)
        self.label_40.setGeometry(QtCore.QRect(10, 46, 91, 21))
        self.label_40.setObjectName("label_40")
        self.op_master_camera_h = QtWidgets.QSpinBox(self.devices)
        self.op_master_camera_h.setGeometry(QtCore.QRect(140, 110, 81, 22))
        self.op_master_camera_h.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.op_master_camera_h.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.op_master_camera_h.setMinimum(0)
        self.op_master_camera_h.setMaximum(15000)
        self.op_master_camera_h.setProperty("value", 1024)
        self.op_master_camera_h.setObjectName("op_master_camera_h")
        self.line_25 = QtWidgets.QFrame(self.devices)
        self.line_25.setGeometry(QtCore.QRect(10, 23, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_25.setFont(font)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setObjectName("line_25")
        self.label_41 = QtWidgets.QLabel(self.devices)
        self.label_41.setGeometry(QtCore.QRect(10, 110, 121, 21))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.devices)
        self.label_42.setGeometry(QtCore.QRect(10, 140, 121, 21))
        self.label_42.setObjectName("label_42")
        self.op_master_camera_w = QtWidgets.QSpinBox(self.devices)
        self.op_master_camera_w.setGeometry(QtCore.QRect(140, 140, 81, 22))
        self.op_master_camera_w.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.op_master_camera_w.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.op_master_camera_w.setMinimum(0)
        self.op_master_camera_w.setMaximum(15000)
        self.op_master_camera_w.setProperty("value", 1024)
        self.op_master_camera_w.setObjectName("op_master_camera_w")
        self.label_43 = QtWidgets.QLabel(self.devices)
        self.label_43.setGeometry(QtCore.QRect(310, 78, 121, 21))
        self.label_43.setObjectName("label_43")
        self.op_slave_camera_w = QtWidgets.QSpinBox(self.devices)
        self.op_slave_camera_w.setGeometry(QtCore.QRect(440, 140, 81, 22))
        self.op_slave_camera_w.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.op_slave_camera_w.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.op_slave_camera_w.setMinimum(0)
        self.op_slave_camera_w.setMaximum(15000)
        self.op_slave_camera_w.setProperty("value", 1024)
        self.op_slave_camera_w.setObjectName("op_slave_camera_w")
        self.line_26 = QtWidgets.QFrame(self.devices)
        self.line_26.setGeometry(QtCore.QRect(310, 23, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_26.setFont(font)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setObjectName("line_26")
        self.label_44 = QtWidgets.QLabel(self.devices)
        self.label_44.setGeometry(QtCore.QRect(310, 140, 121, 21))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.devices)
        self.label_45.setGeometry(QtCore.QRect(310, 110, 121, 21))
        self.label_45.setObjectName("label_45")
        self.label_164 = QtWidgets.QLabel(self.devices)
        self.label_164.setGeometry(QtCore.QRect(310, 8, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_164.setFont(font)
        self.label_164.setObjectName("label_164")
        self.op_slave_fl = QtWidgets.QSpinBox(self.devices)
        self.op_slave_fl.setGeometry(QtCore.QRect(440, 46, 81, 22))
        self.op_slave_fl.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.op_slave_fl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.op_slave_fl.setMinimum(1)
        self.op_slave_fl.setMaximum(10000)
        self.op_slave_fl.setSingleStep(100)
        self.op_slave_fl.setProperty("value", 800)
        self.op_slave_fl.setObjectName("op_slave_fl")
        self.label_46 = QtWidgets.QLabel(self.devices)
        self.label_46.setGeometry(QtCore.QRect(310, 46, 91, 21))
        self.label_46.setObjectName("label_46")
        self.op_slave_camera_h = QtWidgets.QSpinBox(self.devices)
        self.op_slave_camera_h.setGeometry(QtCore.QRect(440, 110, 81, 22))
        self.op_slave_camera_h.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.op_slave_camera_h.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.op_slave_camera_h.setMinimum(0)
        self.op_slave_camera_h.setMaximum(15000)
        self.op_slave_camera_h.setProperty("value", 1024)
        self.op_slave_camera_h.setObjectName("op_slave_camera_h")
        self.op_master_pixel_size = QtWidgets.QDoubleSpinBox(self.devices)
        self.op_master_pixel_size.setGeometry(QtCore.QRect(140, 78, 81, 22))
        self.op_master_pixel_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.op_master_pixel_size.setSingleStep(0.1)
        self.op_master_pixel_size.setProperty("value", 3.76)
        self.op_master_pixel_size.setObjectName("op_master_pixel_size")
        self.op_lat_deg = QtWidgets.QLineEdit(self.devices)
        self.op_lat_deg.setGeometry(QtCore.QRect(80, 223, 51, 34))
        self.op_lat_deg.setObjectName("op_lat_deg")
        self.op_lat_min = QtWidgets.QLineEdit(self.devices)
        self.op_lat_min.setGeometry(QtCore.QRect(140, 223, 51, 34))
        self.op_lat_min.setObjectName("op_lat_min")
        self.op_lat_sec = QtWidgets.QLineEdit(self.devices)
        self.op_lat_sec.setGeometry(QtCore.QRect(200, 223, 51, 34))
        self.op_lat_sec.setObjectName("op_lat_sec")
        self.label_47 = QtWidgets.QLabel(self.devices)
        self.label_47.setGeometry(QtCore.QRect(10, 233, 71, 21))
        self.label_47.setObjectName("label_47")
        self.op_lat_ns = QtWidgets.QComboBox(self.devices)
        self.op_lat_ns.setGeometry(QtCore.QRect(260, 223, 121, 34))
        self.op_lat_ns.setObjectName("op_lat_ns")
        self.op_lat_ns.addItem("")
        self.op_lat_ns.addItem("")
        self.op_lon_deg = QtWidgets.QLineEdit(self.devices)
        self.op_lon_deg.setGeometry(QtCore.QRect(80, 263, 51, 34))
        self.op_lon_deg.setObjectName("op_lon_deg")
        self.op_lon_eo = QtWidgets.QComboBox(self.devices)
        self.op_lon_eo.setGeometry(QtCore.QRect(260, 263, 121, 34))
        self.op_lon_eo.setObjectName("op_lon_eo")
        self.op_lon_eo.addItem("")
        self.op_lon_eo.addItem("")
        self.op_lon_sec = QtWidgets.QLineEdit(self.devices)
        self.op_lon_sec.setGeometry(QtCore.QRect(200, 263, 51, 34))
        self.op_lon_sec.setObjectName("op_lon_sec")
        self.op_lon_min = QtWidgets.QLineEdit(self.devices)
        self.op_lon_min.setGeometry(QtCore.QRect(140, 263, 51, 34))
        self.op_lon_min.setObjectName("op_lon_min")
        self.label_48 = QtWidgets.QLabel(self.devices)
        self.label_48.setGeometry(QtCore.QRect(10, 270, 71, 21))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.devices)
        self.label_49.setGeometry(QtCore.QRect(200, 307, 91, 21))
        self.label_49.setObjectName("label_49")
        self.op_mpc_code = QtWidgets.QLineEdit(self.devices)
        self.op_mpc_code.setGeometry(QtCore.QRect(270, 300, 111, 34))
        self.op_mpc_code.setText("")
        self.op_mpc_code.setObjectName("op_mpc_code")
        self.line_30 = QtWidgets.QFrame(self.devices)
        self.line_30.setGeometry(QtCore.QRect(10, 198, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_30.setFont(font)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setObjectName("line_30")
        self.label_168 = QtWidgets.QLabel(self.devices)
        self.label_168.setGeometry(QtCore.QRect(10, 183, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_168.setFont(font)
        self.label_168.setObjectName("label_168")
        self.op_slave_pixel_size = QtWidgets.QDoubleSpinBox(self.devices)
        self.op_slave_pixel_size.setGeometry(QtCore.QRect(440, 80, 81, 22))
        self.op_slave_pixel_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.op_slave_pixel_size.setSingleStep(0.1)
        self.op_slave_pixel_size.setProperty("value", 3.76)
        self.op_slave_pixel_size.setObjectName("op_slave_pixel_size")
        self.label_50 = QtWidgets.QLabel(self.devices)
        self.label_50.setGeometry(QtCore.QRect(10, 306, 71, 21))
        self.label_50.setObjectName("label_50")
        self.op_altitude = QtWidgets.QLineEdit(self.devices)
        self.op_altitude.setGeometry(QtCore.QRect(80, 300, 111, 34))
        self.op_altitude.setObjectName("op_altitude")
        self.refresh = QtWidgets.QPushButton(self.devices)
        self.refresh.setGeometry(QtCore.QRect(390, 295, 131, 41))
        self.refresh.setObjectName("refresh")
        self.tabWidget.addTab(self.devices, "")
        self.seq = QtWidgets.QWidget()
        self.seq.setObjectName("seq")
        self.op_focus = QtWidgets.QCheckBox(self.seq)
        self.op_focus.setGeometry(QtCore.QRect(20, 50, 191, 24))
        self.op_focus.setChecked(True)
        self.op_focus.setObjectName("op_focus")
        self.op_slew = QtWidgets.QCheckBox(self.seq)
        self.op_slew.setGeometry(QtCore.QRect(20, 190, 241, 24))
        self.op_slew.setChecked(True)
        self.op_slew.setObjectName("op_slew")
        self.op_dithering = QtWidgets.QCheckBox(self.seq)
        self.op_dithering.setGeometry(QtCore.QRect(20, 290, 211, 24))
        self.op_dithering.setChecked(True)
        self.op_dithering.setObjectName("op_dithering")
        self.op_use_autoguiding_master = QtWidgets.QRadioButton(self.seq)
        self.op_use_autoguiding_master.setGeometry(QtCore.QRect(50, 240, 191, 22))
        self.op_use_autoguiding_master.setChecked(True)
        self.op_use_autoguiding_master.setObjectName("op_use_autoguiding_master")
        self.op_autofocus_master = QtWidgets.QCheckBox(self.seq)
        self.op_autofocus_master.setGeometry(QtCore.QRect(50, 80, 171, 22))
        self.op_autofocus_master.setChecked(True)
        self.op_autofocus_master.setObjectName("op_autofocus_master")
        self.op_autofocus_slave = QtWidgets.QCheckBox(self.seq)
        self.op_autofocus_slave.setGeometry(QtCore.QRect(50, 100, 171, 22))
        self.op_autofocus_slave.setChecked(True)
        self.op_autofocus_slave.setObjectName("op_autofocus_slave")
        self.op_use_autoguiding_slave = QtWidgets.QRadioButton(self.seq)
        self.op_use_autoguiding_slave.setGeometry(QtCore.QRect(50, 260, 171, 22))
        self.op_use_autoguiding_slave.setObjectName("op_use_autoguiding_slave")
        self.op_autoconnect = QtWidgets.QCheckBox(self.seq)
        self.op_autoconnect.setGeometry(QtCore.QRect(20, 310, 171, 22))
        self.op_autoconnect.setObjectName("op_autoconnect")
        self.op_calibrate_use_filter = QtWidgets.QCheckBox(self.seq)
        self.op_calibrate_use_filter.setGeometry(QtCore.QRect(330, 120, 241, 22))
        self.op_calibrate_use_filter.setObjectName("op_calibrate_use_filter")
        self.op_close_shutter = QtWidgets.QCheckBox(self.seq)
        self.op_close_shutter.setGeometry(QtCore.QRect(310, 70, 171, 22))
        self.op_close_shutter.setObjectName("op_close_shutter")
        self.op_calibrate_at_the_end = QtWidgets.QCheckBox(self.seq)
        self.op_calibrate_at_the_end.setGeometry(QtCore.QRect(310, 90, 221, 22))
        self.op_calibrate_at_the_end.setObjectName("op_calibrate_at_the_end")
        self.op_calibrate_close_shutter = QtWidgets.QCheckBox(self.seq)
        self.op_calibrate_close_shutter.setGeometry(QtCore.QRect(330, 190, 241, 22))
        self.op_calibrate_close_shutter.setObjectName("op_calibrate_close_shutter")
        self.op_warm = QtWidgets.QCheckBox(self.seq)
        self.op_warm.setGeometry(QtCore.QRect(310, 50, 171, 22))
        self.op_warm.setObjectName("op_warm")
        self.label_165 = QtWidgets.QLabel(self.seq)
        self.label_165.setGeometry(QtCore.QRect(310, 15, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_165.setFont(font)
        self.label_165.setObjectName("label_165")
        self.line_27 = QtWidgets.QFrame(self.seq)
        self.line_27.setGeometry(QtCore.QRect(310, 30, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_27.setFont(font)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setObjectName("line_27")
        self.label_166 = QtWidgets.QLabel(self.seq)
        self.label_166.setGeometry(QtCore.QRect(20, 15, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_166.setFont(font)
        self.label_166.setObjectName("label_166")
        self.line_28 = QtWidgets.QFrame(self.seq)
        self.line_28.setGeometry(QtCore.QRect(20, 30, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_28.setFont(font)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setObjectName("line_28")
        self.line_29 = QtWidgets.QFrame(self.seq)
        self.line_29.setGeometry(QtCore.QRect(20, 165, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_29.setFont(font)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setObjectName("line_29")
        self.label_167 = QtWidgets.QLabel(self.seq)
        self.label_167.setGeometry(QtCore.QRect(20, 150, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_167.setFont(font)
        self.label_167.setObjectName("label_167")
        self.op_selected_filter = QtWidgets.QComboBox(self.seq)
        self.op_selected_filter.setGeometry(QtCore.QRect(360, 150, 161, 34))
        self.op_selected_filter.setObjectName("op_selected_filter")
        self.op_guiding = QtWidgets.QCheckBox(self.seq)
        self.op_guiding.setGeometry(QtCore.QRect(20, 210, 191, 24))
        self.op_guiding.setObjectName("op_guiding")
        self.tabWidget.addTab(self.seq, "")
        self.label_169 = QtWidgets.QLabel(SaaSOptions)
        self.label_169.setGeometry(QtCore.QRect(10, 19, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_169.setFont(font)
        self.label_169.setObjectName("label_169")
        self.line_31 = QtWidgets.QFrame(SaaSOptions)
        self.line_31.setGeometry(QtCore.QRect(10, 34, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_31.setFont(font)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setObjectName("line_31")
        self.master_profile = QtWidgets.QComboBox(SaaSOptions)
        self.master_profile.setGeometry(QtCore.QRect(10, 61, 161, 32))
        self.master_profile.setCurrentText("")
        self.master_profile.setObjectName("master_profile")
        self.master_adv_options = QtWidgets.QPushButton(SaaSOptions)
        self.master_adv_options.setGeometry(QtCore.QRect(180, 60, 41, 34))
        self.master_adv_options.setObjectName("master_adv_options")
        self.label_170 = QtWidgets.QLabel(SaaSOptions)
        self.label_170.setGeometry(QtCore.QRect(320, 20, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_170.setFont(font)
        self.label_170.setObjectName("label_170")
        self.slave_profile = QtWidgets.QComboBox(SaaSOptions)
        self.slave_profile.setGeometry(QtCore.QRect(320, 62, 161, 32))
        self.slave_profile.setCurrentText("")
        self.slave_profile.setObjectName("slave_profile")
        self.slave_adv_options = QtWidgets.QPushButton(SaaSOptions)
        self.slave_adv_options.setGeometry(QtCore.QRect(490, 60, 41, 34))
        self.slave_adv_options.setObjectName("slave_adv_options")
        self.line_32 = QtWidgets.QFrame(SaaSOptions)
        self.line_32.setGeometry(QtCore.QRect(320, 35, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_32.setFont(font)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_32.setObjectName("line_32")

        self.retranslateUi(SaaSOptions)
        self.tabWidget.setCurrentIndex(0)
        self.master_profile.setCurrentIndex(-1)
        self.slave_profile.setCurrentIndex(-1)
        self.buttonBox.accepted.connect(SaaSOptions.accept)
        self.buttonBox.rejected.connect(SaaSOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(SaaSOptions)

    def retranslateUi(self, SaaSOptions):
        _translate = QtCore.QCoreApplication.translate
        SaaSOptions.setWindowTitle(_translate("SaaSOptions", "SaaS Options"))
        self.op_master_fl.setToolTip(_translate("SaaSOptions", "Sets the camera bin"))
        self.label_163.setText(_translate("SaaSOptions", "Master"))
        self.label_39.setText(_translate("SaaSOptions", "Camera pixel size"))
        self.label_40.setText(_translate("SaaSOptions", "Focal lenght"))
        self.op_master_camera_h.setToolTip(_translate("SaaSOptions", "Sets number of frames needed to dither"))
        self.label_41.setText(_translate("SaaSOptions", "Camera pixels (H)"))
        self.label_42.setText(_translate("SaaSOptions", "Camera pixels (W)"))
        self.op_master_camera_w.setToolTip(_translate("SaaSOptions", "Sets number of frames needed to dither"))
        self.label_43.setText(_translate("SaaSOptions", "Camera pixel size"))
        self.op_slave_camera_w.setToolTip(_translate("SaaSOptions", "Sets number of frames needed to dither"))
        self.label_44.setText(_translate("SaaSOptions", "Camera pixels (W)"))
        self.label_45.setText(_translate("SaaSOptions", "Camera pixels (H)"))
        self.label_164.setText(_translate("SaaSOptions", "Slave"))
        self.op_slave_fl.setToolTip(_translate("SaaSOptions", "Sets the camera bin"))
        self.label_46.setText(_translate("SaaSOptions", "Focal lenght"))
        self.op_slave_camera_h.setToolTip(_translate("SaaSOptions", "Sets number of frames needed to dither"))
        self.label_47.setText(_translate("SaaSOptions", "Latitude"))
        self.op_lat_ns.setItemText(0, _translate("SaaSOptions", "North"))
        self.op_lat_ns.setItemText(1, _translate("SaaSOptions", "South"))
        self.op_lon_eo.setItemText(0, _translate("SaaSOptions", "East"))
        self.op_lon_eo.setItemText(1, _translate("SaaSOptions", "West"))
        self.label_48.setText(_translate("SaaSOptions", "Longitude"))
        self.label_49.setText(_translate("SaaSOptions", "MPC Code"))
        self.label_168.setText(_translate("SaaSOptions", "Observer"))
        self.label_50.setText(_translate("SaaSOptions", "Altitude"))
        self.refresh.setText(_translate("SaaSOptions", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.devices), _translate("SaaSOptions", "Devices"))
        self.op_focus.setText(_translate("SaaSOptions", "Enable sequence focus"))
        self.op_slew.setText(_translate("SaaSOptions", "Slew/sync to object coordinates"))
        self.op_dithering.setText(_translate("SaaSOptions", "Enable dithering"))
        self.op_use_autoguiding_master.setText(_translate("SaaSOptions", "Autoguide from master"))
        self.op_autofocus_master.setText(_translate("SaaSOptions", "Autofocus master"))
        self.op_autofocus_slave.setText(_translate("SaaSOptions", "Autofocus slave"))
        self.op_use_autoguiding_slave.setText(_translate("SaaSOptions", "Autoguide from slave"))
        self.op_autoconnect.setText(_translate("SaaSOptions", "Autoconnect devices"))
        self.op_calibrate_use_filter.setText(_translate("SaaSOptions", "User filter (dark and bias)"))
        self.op_close_shutter.setText(_translate("SaaSOptions", "Close shuter"))
        self.op_calibrate_at_the_end.setText(_translate("SaaSOptions", "Capture calibration frames"))
        self.op_calibrate_close_shutter.setText(_translate("SaaSOptions", "Close shuter"))
        self.op_warm.setText(_translate("SaaSOptions", "Warm camera"))
        self.label_165.setText(_translate("SaaSOptions", "End of sequence"))
        self.label_166.setText(_translate("SaaSOptions", "Focus"))
        self.label_167.setText(_translate("SaaSOptions", "Features"))
        self.op_guiding.setText(_translate("SaaSOptions", "Enable autoguiding"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.seq), _translate("SaaSOptions", "Sequence"))
        self.label_169.setText(_translate("SaaSOptions", "Master Profile"))
        self.master_adv_options.setText(_translate("SaaSOptions", "..."))
        self.label_170.setText(_translate("SaaSOptions", "Slave Profile"))
        self.slave_adv_options.setText(_translate("SaaSOptions", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SaaSOptions = QtWidgets.QDialog()
    ui = Ui_SaaSOptions()
    ui.setupUi(SaaSOptions)
    SaaSOptions.show()
    sys.exit(app.exec_())
