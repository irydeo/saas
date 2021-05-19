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
from datetime import date, datetime
from datetime import datetime, timedelta

from ui.wait_ui import Ui_Wait


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

        # Set correct dates
        self.ts_selected_time.setDateTime(datetime.now())
        self.ts_discovery_date.setDateTime(datetime.today() - timedelta(days=30)) # One month range by default
        self.neo_selected_time.setDateTime(datetime.now())

        # Connect
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
        selected = self.neo_data.currentIndex()
        if not selected.isValid() or len(self.neo_data.selectedItems()) < 1:
            return

        self.options.set("object_name", self.neo_data.item(self.neo_data.currentRow(), 0).text())

        # Set master and slave exposure times
        self.options.set("master_single_exposure", int(self.neo_data.item(self.neo_data.currentRow(), 4).text()))
        print(self.neo_data.item(self.neo_data.currentRow(), 4).text())
        self.options.set("slave_single_exposure", int(self.neo_data.item(self.neo_data.currentRow(), 5).text()))
        print(self.neo_data.item(self.neo_data.currentRow(), 5).text())

        # Current AR/DEC
        self.options.set("ar", self.neo.get_current_ardec(self.neo_data.item(self.neo_data.currentRow(), 0).text())[0])
        self.options.set("dec", self.neo.get_current_ardec(self.neo_data.item(self.neo_data.currentRow(), 0).text())[1])

    def ts_selected(self):
        selected = self.ts_data.currentIndex()
        if not selected.isValid() or len(self.ts_data.selectedItems()) < 1:
            return

        self.options.set("object_name", self.ts_data.item(self.ts_data.currentRow(), 0).text())
        self.options.set("ar", self.ts_data.item(self.ts_data.currentRow(), 5).text())
        self.options.set("dec", self.ts_data.item(self.ts_data.currentRow(), 6).text())

    def update_neo_db(self):
        msg = "Do you want to fully update NEOs database for " + self.neo_selected_time.text() + "?"
        reply = QMessageBox.question(self.dialog, 'Update NEOs database',
                                     msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            dialog = QtWidgets.QDialog()
            dialog.ui = Ui_Wait()
            dialog.ui.setupUi(dialog)

            thread = threading.Thread(target=self.update_neo_db_thread, args=(dialog,))
            thread.start()

            dialog.exec_()
            #dialog.show()


    def update_neo_db_thread(self, d):
        d.ui.msg.setText("Updating NEOs database at " + self.neo_selected_time.text())
        self.update_prio_list.setEnabled(False)
        self.neo.update()
        self.update_prio_list.setEnabled(True)
        d.ui.msg.setText("Finished...")
        d.hide()


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

    def fill_neo_table(self, event, limit_magnitude=21, n_values=100, min_altitude=20):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            index = 0
            self.neo_data.reset()
            self.neo.set_time(self.neo_selected_time.dateTime().toPyDateTime())
            master_resolution = self.calculate_resolution(self.options.get("op_master_pixel_size", 9),
                                                          self.options.get("op_master_fl", 1800))
            slave_resolution = self.calculate_resolution(self.options.get("op_slave_pixel_size", 9),
                                                          self.options.get("op_slave_fl", 1800))

            if len(str.strip(self.neo_name.text())) == 0:
                # TODO: Date ops
                query = 'SELECT name, prio, motion, m FROM neo where m<?  ORDER BY prio ASC limit ?'
            else:
                query = 'SELECT name, prio, motion, m FROM neo where m<?  and name LIKE \'%' + self.neo_name.text() + '%\' ORDER BY prio ASC limit ?'

            #for row in c.execute('SELECT name, prio, alt, motion, m FROM neo where m<? and alt>?  ORDER BY prio ASC limit ?',
            #                     (str(limit_magnitude), str(min_altitude), str(n_values))):
            for row in c.execute(query, (str(self.neo_magnitude.value()), str(n_values))):
                # First, get altitude
                altitude = self.neo.get_current_altitude(str(row[0]))
                if altitude >= self.neo_altitude.value():
                    self.neo_data.setRowCount(index+1)
                    self.neo_data.setItem(index, 0, QTableWidgetItem(str(row[0])))
                    self.neo_data.setItem(index, 1, QTableWidgetItem(str(row[1])))

                    self.neo_data.setItem(index, 2, QTableWidgetItem(str(altitude)))
                    self.neo_data.setItem(index, 3, QTableWidgetItem(str(round(row[2],2))))

                    # TODO: Calculate current altidude here, in fact, add a button to update ephemerids on dialog, does it make sense to do it when update?

                    self.neo_data.setItem(index, 4, QTableWidgetItem(str(int(master_resolution / (row[2] / 60)))))
                    self.neo_data.setItem(index, 5, QTableWidgetItem(str(int(slave_resolution / (row[2] / 60)))))
                    self.neo_data.setItem(index, 6, QTableWidgetItem(str(row[3])))

                    # Current AR/DEC
                    coords = self.neo.get_current_ardec(str(row[0]))
                    self.neo_data.setItem(index, 7, QTableWidgetItem(coords[0]))
                    self.neo_data.setItem(index, 8, QTableWidgetItem(coords[1]))

                    diagonal_size = 0.54
                    size_arcsec = 3600 * diagonal_size
                    motion_arcsec_per_minute = row[2]
                    max_exp_time_minutes = (size_arcsec / motion_arcsec_per_minute) / 2 # by two, considering at start is in the middle/centered
                    self.neo_data.setItem(index, 9, QTableWidgetItem(str(round(max_exp_time_minutes))))

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
            self.sn.set_time(self.ts_selected_time.dateTime().toPyDateTime())

            if len(str.strip(self.ts_name.text())) == 0:
                #query = 'SELECT name, m, type, date, ra, dec, host FROM sn where m<? and date >? ORDER BY date DESC'
                # TODO: Date ops
                query = 'SELECT name, m, type, date, ra, dec, host FROM sn where m<?  ORDER BY date DESC limit ?'
            else:
                query = 'SELECT name, m, type, date, ra, dec, host FROM sn where m<? and name LIKE \'%' + self.ts_name.text() + '%\' ORDER BY date DESC limit ?'

            #portion = (self.ts_discovery_date.time().hour() /24)
            #q_day = self.ts_discovery_date.date().day() + (self.ts_discovery_date.time().hour() /24)
            #q_date = str(self.ts_discovery_date.date().year()) +"/" + str(self.ts_discovery_date.date().month()) +"/" + str(q_day)
            #print(q_date)

            for row in c.execute(query, (str(self.ts_magnitude.value()),n_values)):
                sn_altitude = self.sn.get_altitude(str(row[4]), str(row[5]))
                if sn_altitude >= self.ts_altitude.value():
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
    ##################
    ## Calculate the resolution in arc seconds per pixel of a CCD with a particular telescope
    ##################
    def calculate_resolution(self, pixel_size, focal_length):
        return (pixel_size/focal_length)* 206.265