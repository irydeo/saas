# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sequence_options_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(457, 268)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 230, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.slaveSystem_2 = QtWidgets.QGroupBox(Dialog)
        self.slaveSystem_2.setGeometry(QtCore.QRect(10, 10, 441, 211))
        self.slaveSystem_2.setTitle("")
        self.slaveSystem_2.setObjectName("slaveSystem_2")
        self.label_7 = QtWidgets.QLabel(self.slaveSystem_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.autofocus_master = QtWidgets.QCheckBox(self.slaveSystem_2)
        self.autofocus_master.setGeometry(QtCore.QRect(40, 100, 171, 22))
        self.autofocus_master.setObjectName("autofocus_master")
        self.use_autoguiding_slave = QtWidgets.QCheckBox(self.slaveSystem_2)
        self.use_autoguiding_slave.setGeometry(QtCore.QRect(40, 80, 171, 22))
        self.use_autoguiding_slave.setObjectName("use_autoguiding_slave")
        self.autofocus_slave = QtWidgets.QCheckBox(self.slaveSystem_2)
        self.autofocus_slave.setGeometry(QtCore.QRect(40, 120, 171, 22))
        self.autofocus_slave.setObjectName("autofocus_slave")
        self.use_autoguiding_master = QtWidgets.QCheckBox(self.slaveSystem_2)
        self.use_autoguiding_master.setGeometry(QtCore.QRect(40, 60, 171, 22))
        self.use_autoguiding_master.setObjectName("use_autoguiding_master")
        self.autofocus_slave_2 = QtWidgets.QCheckBox(self.slaveSystem_2)
        self.autofocus_slave_2.setGeometry(QtCore.QRect(230, 40, 171, 22))
        self.autofocus_slave_2.setObjectName("autofocus_slave_2")
        self.autofocus_slave_3 = QtWidgets.QCheckBox(self.slaveSystem_2)
        self.autofocus_slave_3.setGeometry(QtCore.QRect(230, 70, 171, 22))
        self.autofocus_slave_3.setObjectName("autofocus_slave_3")
        self.autofocus_slave_4 = QtWidgets.QCheckBox(self.slaveSystem_2)
        self.autofocus_slave_4.setGeometry(QtCore.QRect(230, 100, 171, 22))
        self.autofocus_slave_4.setObjectName("autofocus_slave_4")
        self.autofocus_slave_5 = QtWidgets.QCheckBox(self.slaveSystem_2)
        self.autofocus_slave_5.setGeometry(QtCore.QRect(230, 120, 171, 22))
        self.autofocus_slave_5.setObjectName("autofocus_slave_5")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "General Options"))
        self.autofocus_master.setText(_translate("Dialog", "Autofocus master"))
        self.use_autoguiding_slave.setText(_translate("Dialog", "Autoguide from slave"))
        self.autofocus_slave.setText(_translate("Dialog", "Autofocus slave"))
        self.use_autoguiding_master.setText(_translate("Dialog", "Autoguide from master"))
        self.autofocus_slave_2.setText(_translate("Dialog", "Autoconnect devices"))
        self.autofocus_slave_3.setText(_translate("Dialog", "Warm camera"))
        self.autofocus_slave_4.setText(_translate("Dialog", "Close shuter"))
        self.autofocus_slave_5.setText(_translate("Dialog", "Run command"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
