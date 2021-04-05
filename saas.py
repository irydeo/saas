import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMessageBox
import time
from ui.main_ui import Ui_MainWindow
from Director import Director
 
class Saas(Ui_MainWindow):
    
    ##################
    ## Init function
    ##################
    def __init__(self, dialog):

        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.dialog = dialog

        self.start.clicked.connect(self.start_click)

        self.director = Director()

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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #dialog = QtWidgets.QDialog()
    dialog = QtWidgets.QMainWindow()
    prog = Saas(dialog)
    dialog.show()
    sys.exit(app.exec_())
