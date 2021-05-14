############################################################
# -*- coding: utf-8 -*-
#
# SAAS main file
#
# Francisco José Calvo Fernández (http://www.irydeo.com)
# (c) 2021
# Licence GPL v3
############################################################
from statistics import mean

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from ui.object_selector_ui import Ui_ObjectSelector
from supernova import Supernova
from neo import NEO
import logging as logger
import threading
import sqlite3
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import datetime


class ObjectSelector(Ui_ObjectSelector):

    ##################
    ## Init function
    ##################
    def __init__(self, dialog, options):
        Ui_ObjectSelector.__init__(self)
        self.setupUi(dialog)
        self.dialog = dialog
        self.db = 'db/saas.db'
        self.sn = Supernova()
        self.neo = NEO()
        self.options = options

        self.update_prio_list.clicked.connect(self.fill_neo_table)
        self.ts_query.clicked.connect(self.fill_ts_table)
        self.update_db.clicked.connect(self.update_neo_db)
        self.ts_update_db.clicked.connect(self.update_ts_db)
        self.neo_data.clicked.connect(self.neo_selected)
        self.ts_data.clicked.connect(self.ts_selected)


        header = self.neo_data.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        header_ts = self.ts_data.horizontalHeader()
        header_ts.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def neo_selected(self):
         print("")

    def ts_selected(self):
        selected = self.ts_data.currentIndex()
        if not selected.isValid() or len(self.ts_data.selectedItems()) < 1:
            return

        self.options.set("object_name", self.ts_data.item(self.ts_data.currentRow(), 0).text())
        self.options.set("ar", self.ts_data.item(self.ts_data.currentRow(), 5).text())
        self.options.set("dec", self.ts_data.item(self.ts_data.currentRow(), 6).text())


    def update_neo_db(self):
        msg = "Do you want to fully update NEOs database?"
        reply = QMessageBox.question(self.dialog, 'Update NEOs database',
                                     msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.neo.update()


    def update_ts_db(self):
        msg = "Do you want to fully update Transients database?"
        reply = QMessageBox.question(self.dialog, 'Update Transients database',
                                     msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            thread = threading.Thread(target=self.sn.update_from_rochesterastronomy)
            thread.start()

            # Show message and disable query buttons
            while thread.is_alive():
                print("Is thread1 alive:")



    def fill_neo_table(self, event, limit_magnitude=21, n_values=50, min_altitude=20):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            index = 0
            self.neo_data.reset()
            for row in c.execute('SELECT name, prio, alt, motion, m FROM neo where m<? and alt>?  ORDER BY prio ASC limit ?',
                                 (str(limit_magnitude), str(min_altitude), str(n_values))):

                print("Result: " + str(row[0]))
                self.neo_data.setRowCount(index+1)
                self.neo_data.setItem(index, 0, QTableWidgetItem(str(row[0])))
                self.neo_data.setItem(index, 1, QTableWidgetItem(str(row[1])))
                self.neo_data.setItem(index, 2, QTableWidgetItem(str(row[2])))
                self.neo_data.setItem(index, 3, QTableWidgetItem(str(row[3])))
                self.neo_data.setItem(index, 4, QTableWidgetItem(str(row[4])))

                index += 1

            conn.close()

        except ValueError:
            logger.error("Error")
        except KeyError:
            logger.error("KeyError")
        except TypeError as err:
            logger.error("TypeError", err)

    def fill_ts_table(self, event, limit_magnitude=21, n_values=250, min_altitude=20):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            index = 0
            self.ts_data.reset()
            for row in c.execute('SELECT name, m, type, date, ra, dec, host FROM sn where m<? ORDER BY date DESC limit ?',
                                 (str(limit_magnitude), str(n_values))):
                sn_altitude = self.sn.get_altitude(str(row[4]), str(row[5]))
                if sn_altitude >= min_altitude:
                    self.ts_data.setRowCount(index+1)
                    self.ts_data.setItem(index, 0, QTableWidgetItem(str(row[0])))
                    self.ts_data.setItem(index, 1, QTableWidgetItem(str(sn_altitude)))
                    self.ts_data.setItem(index, 2, QTableWidgetItem(str(row[1])))
                    self.ts_data.setItem(index, 3, QTableWidgetItem(str(row[2])))
                    self.ts_data.setItem(index, 4, QTableWidgetItem(str(row[3])))
                    self.ts_data.setItem(index, 5, QTableWidgetItem(str(row[4])))
                    self.ts_data.setItem(index, 6, QTableWidgetItem(str(row[5])))
                    self.ts_data.setItem(index, 7, QTableWidgetItem(str(row[6])))

                    index += 1

            conn.close()

        except ValueError:
            logger.error("Error")
        except KeyError:
            logger.error("KeyError")
        except TypeError as err:
            logger.error("TypeError", err)