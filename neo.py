############################################################
# -*- coding: utf-8 -*-
#
# SAAS NEOs module
# Python  v3.9
#
# Francisco José Calvo Fernández
# (c) 2017-2021
#
# Licence GPL v3
#
############################################################
from astroquery.mpc import MPC
from datetime import datetime
from pprint import pprint
import erfa
import urllib
import sqlite3


class NEO:

    def __init__(self):
        self.db = 'db/saas.db'
        self.url = 'https://neo.ssa.esa.int/PSDB-portlet/download?file=esa_priority_neo_list'
        self.lat = 40
        self.lon = -3
        self.height = 631
        self.utcoffset = 0

    # Set user coords to correctly calculate sn visibility when requested
    # @args:
    #   1. lat - float (user latitude)
    #   2. lon - float (user longitude)
    #   3. height - integer (location height over sea level in meters)
    #   4. utcoffset - integer (offset to utc hour)
    def set_coords(self, lat, lon, height=0, utcoffset=0):
        self.lat = lat
        self.lon = lon
        self.height = height
        self.utcoffset = utcoffset

    # Read priority list from https://neo.ssa.esa.int/ PSDB-portlet/download?file=esa_priority_neo_list
    # @args:
    #   none
    def get_priority_list(self):
        urllib.request.urlretrieve(self.url, "plist.txt")

    # Update latest NEOs in priority list
    # @args:
    #   1. location_p - string (MPC user observatory)
    #   2. start_p - datetime (2021-05-12 22:00:00)
    #   3. step_p - string (steps in m, s, h, d...)
    #   4. number_p - string (number of calculated ephemerids)
    def update(self, location_p='Z41', start_p=datetime.now(), step_p='1h', number_p=1):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()

            urllib.request.urlretrieve(self.url, "plist.txt")

            with open("plist.txt", "r") as f:
                data = f.readlines()
                c.execute("DELETE from neo")
                for line in data:
                    if len(line) > 41:
                        prio = line[0:2]
                        name = line[3:16]
                        name = name.replace("\"", "")
                        ra = (float(line[17:25].strip()) / 60) / 60  # From seg to hours
                        dec = line[26:31].strip()
                        elong = line[32:35]
                        m = line[36:40]
                        date = line[48:60]
                        date = date.replace("\"", "")

                        #eph = MPC.get_ephemeris(name, location='Z41', start='2021-05-12 22:00:00', step='1h', number=1)
                        eph = MPC.get_ephemeris(name, location=location_p, start=start_p, step=step_p,
                                                number=number_p)
                        altitude = eph['Altitude'].max()
                        motion = eph['Proper motion'].max()
                        mag = eph['V'].max()

                        # TODO: Calculate rating
                        c.execute(
                            "INSERT OR IGNORE INTO neo (name, prio, ra, dec, m, elong, date, alt, motion, mag)  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (name.strip(), prio, ra, dec, m, elong, date, float(altitude), float(motion), float(mag)))
                        # select prio, name, max_alt, mag, motion from neo WHERE alt > 40 and mag < 20;
        except ValueError:
            print("ValueError")
        except KeyError:
            print("KeyError")
        except TypeError:
            print("TypeError")

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

