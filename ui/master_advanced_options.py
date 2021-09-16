# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'master_advanced_options.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MasterAdvancedOptions(object):
    def setupUi(self, MasterAdvancedOptions):
        MasterAdvancedOptions.setObjectName("MasterAdvancedOptions")
        MasterAdvancedOptions.resize(284, 287)
        MasterAdvancedOptions.setMaximumSize(QtCore.QSize(284, 287))
        self.buttonBox = QtWidgets.QDialogButtonBox(MasterAdvancedOptions)
        self.buttonBox.setGeometry(QtCore.QRect(50, 250, 231, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_166 = QtWidgets.QLabel(MasterAdvancedOptions)
        self.label_166.setGeometry(QtCore.QRect(130, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_166.setFont(font)
        self.label_166.setObjectName("label_166")
        self.label_165 = QtWidgets.QLabel(MasterAdvancedOptions)
        self.label_165.setGeometry(QtCore.QRect(20, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_165.setFont(font)
        self.label_165.setObjectName("label_165")
        self.master_host = QtWidgets.QLineEdit(MasterAdvancedOptions)
        self.master_host.setGeometry(QtCore.QRect(20, 60, 101, 32))
        self.master_host.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.master_host.setObjectName("master_host")
        self.master_port = QtWidgets.QLineEdit(MasterAdvancedOptions)
        self.master_port.setGeometry(QtCore.QRect(130, 60, 101, 32))
        self.master_port.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.master_port.setObjectName("master_port")
        self.sm_burst_options = QtWidgets.QGroupBox(MasterAdvancedOptions)
        self.sm_burst_options.setEnabled(True)
        self.sm_burst_options.setGeometry(QtCore.QRect(20, 130, 221, 101))
        self.sm_burst_options.setTitle("")
        self.sm_burst_options.setFlat(True)
        self.sm_burst_options.setObjectName("sm_burst_options")
        self.fo_3 = QtWidgets.QLabel(self.sm_burst_options)
        self.fo_3.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.fo_3.setFont(font)
        self.fo_3.setObjectName("fo_3")
        self.sm_group_every = QtWidgets.QSpinBox(self.sm_burst_options)
        self.sm_group_every.setGeometry(QtCore.QRect(140, 10, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sm_group_every.setFont(font)
        self.sm_group_every.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sm_group_every.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sm_group_every.setMinimum(0)
        self.sm_group_every.setMaximum(720)
        self.sm_group_every.setProperty("value", 1)
        self.sm_group_every.setObjectName("sm_group_every")
        self.sm_group_delay = QtWidgets.QSpinBox(self.sm_burst_options)
        self.sm_group_delay.setGeometry(QtCore.QRect(140, 40, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sm_group_delay.setFont(font)
        self.sm_group_delay.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sm_group_delay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sm_group_delay.setMinimum(0)
        self.sm_group_delay.setMaximum(100)
        self.sm_group_delay.setProperty("value", 1)
        self.sm_group_delay.setObjectName("sm_group_delay")
        self.fo_5 = QtWidgets.QLabel(self.sm_burst_options)
        self.fo_5.setGeometry(QtCore.QRect(10, 40, 131, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.fo_5.setFont(font)
        self.fo_5.setObjectName("fo_5")
        self.sm_group_keyword = QtWidgets.QLineEdit(self.sm_burst_options)
        self.sm_group_keyword.setGeometry(QtCore.QRect(140, 73, 71, 21))
        self.sm_group_keyword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sm_group_keyword.setObjectName("sm_group_keyword")
        self.fo_7 = QtWidgets.QLabel(self.sm_burst_options)
        self.fo_7.setGeometry(QtCore.QRect(10, 73, 131, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.fo_7.setFont(font)
        self.fo_7.setObjectName("fo_7")
        self.line_34 = QtWidgets.QFrame(MasterAdvancedOptions)
        self.line_34.setGeometry(QtCore.QRect(20, 115, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_34.setFont(font)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_34.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_34.setObjectName("line_34")
        self.label_176 = QtWidgets.QLabel(MasterAdvancedOptions)
        self.label_176.setGeometry(QtCore.QRect(20, 100, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_176.setFont(font)
        self.label_176.setObjectName("label_176")
        self.label_177 = QtWidgets.QLabel(MasterAdvancedOptions)
        self.label_177.setGeometry(QtCore.QRect(20, 5, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_177.setFont(font)
        self.label_177.setObjectName("label_177")
        self.line_35 = QtWidgets.QFrame(MasterAdvancedOptions)
        self.line_35.setGeometry(QtCore.QRect(20, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_35.setFont(font)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_35.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_35.setObjectName("line_35")

        self.retranslateUi(MasterAdvancedOptions)
        self.buttonBox.accepted.connect(MasterAdvancedOptions.accept)
        self.buttonBox.rejected.connect(MasterAdvancedOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(MasterAdvancedOptions)

    def retranslateUi(self, MasterAdvancedOptions):
        _translate = QtCore.QCoreApplication.translate
        MasterAdvancedOptions.setWindowTitle(_translate("MasterAdvancedOptions", "Advanced Options (Master)"))
        self.label_166.setText(_translate("MasterAdvancedOptions", "Port"))
        self.label_165.setText(_translate("MasterAdvancedOptions", "Server"))
        self.master_host.setText(_translate("MasterAdvancedOptions", "localhost"))
        self.master_port.setText(_translate("MasterAdvancedOptions", "3277"))
        self.fo_3.setText(_translate("MasterAdvancedOptions", "Group every:"))
        self.sm_group_every.setToolTip(_translate("MasterAdvancedOptions", "Group every selected number of frames"))
        self.sm_group_delay.setToolTip(_translate("MasterAdvancedOptions", "Delay between groups"))
        self.fo_5.setText(_translate("MasterAdvancedOptions", "Grouping delay:"))
        self.sm_group_keyword.setText(_translate("MasterAdvancedOptions", "GROUP"))
        self.fo_7.setText(_translate("MasterAdvancedOptions", "Grouping keyword:"))
        self.label_176.setText(_translate("MasterAdvancedOptions", "Burst options"))
        self.label_177.setText(_translate("MasterAdvancedOptions", "CCDCiel host"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MasterAdvancedOptions = QtWidgets.QDialog()
    ui = Ui_MasterAdvancedOptions()
    ui.setupUi(MasterAdvancedOptions)
    MasterAdvancedOptions.show()
    sys.exit(app.exec_())
