############################################################
# -*- coding: utf-8 -*-
#
# SAAS Supernova module
# Python  v3.9
#
# Francisco José Calvo Fernández
# (c) 2017-2021
#
# Licence GPL v3
#
############################################################

import logging as logger
from urllib import request
import json
import re
import sqlite3
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import datetime
import requests
import lxml.html as lh


class Supernova:

    def __init__(self):
        self.db = 'db/saas.db'
        self.snurl_sne = 'https://sne.space/astrocats/astrocats/supernovae/output/catalog.min.json'
        self.snurl_rs = 'https://www.rochesterastronomy.org/snimages/sndate.html'
        self.lat=40
        self.lon=-3
        self.height=631
        self.utcoffset=0
        self.q_time = datetime.datetime.now()

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

    def set_time(self, q_time):
        self.q_time = q_time

    # Update latest supernovae from sne.space. It is a but outdated, so it is not recommended.
    # @args:
    #   none
    def update_from_sne(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        sn_results = []

        req = request.Request(self.snurl_sne)
        with request.urlopen(req) as f:
                            captureResponse = json.loads(f.read().decode('utf-8'))

        for sn in captureResponse:
            try:
                sn_date= sn['discoverdate'][0]['value']
                mag = float(sn['maxappmag'][0]['value'].strip())
                host = sn['host'][0]['value']
                ra = sn['ra'][0]['value']
                dec = sn['dec'][0]['value']
                type = sn['claimedtype'][0]['value']
                print(sn['name'])
                if re.match('\d\d\d\d/\d\d\/\d\d', sn_date):
                    # Insert a row of data
                    c.execute("INSERT OR IGNORE INTO sn (name, date, m, host, ra, dec, type)  VALUES (?, ?, ?, ?, ?, ?, ?)",  
                    (sn['name'],  sn_date,  mag,  host,  str(ra),  str(dec),   str(type)))
                    #self.checkVisibility( ra,  dec)

            except ValueError:
                logger.error("ValueError")
            except KeyError:
                logger.error("KeyError")
            except TypeError:
                logger.error("TypeError")
                
        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    # Update latest supernovae from https://www.rochesterastronomy.org/, by David Bishop. Currently, best source of SN information.
    # @args:
    #   none
    def update_from_rochesterastronomy(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        # Create a handle, page, to handle the contents of the website
        page = requests.get(self.snurl_rs)
        # Store the contents of the website under doc
        doc = lh.fromstring(page.content)
        # Parse data that are stored between <tr>..</tr> of HTML
        tr_elements = doc.xpath('/html/body/table[2]//tr')

        # For each row, store each first element (header) and an empty list
        for t in tr_elements:
            try:
                date= t[2].text_content()
                mag = float(t[8].text_content())
                host = t[6].text_content()
                ra = t[0].text_content()
                dec = t[1].text_content()
                sn_type = t[7].text_content()
                name = t[10].text_content()

                if re.match('\d\d\d\d/\d\d\/\d\d', date):
                    # Insert a row of data
                    c.execute("INSERT OR IGNORE INTO sn (name, date, m, host, ra, dec, type)  VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (name,  date,  mag,  host,  str(ra),  str(dec),   str(sn_type)))

            except ValueError:
                logger.error("ValueError")
            except KeyError:
                logger.error("KeyError")
            except TypeError:
                logger.error("TypeError")

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    # Return list of latest visible supernova, from user location
    # @args:
    #   1. minAlt - integer (min altitude)
    #   2. limitMagnitude - float (max sn magnitude)
    #   3. dateTime - date
    #   4. nValues - integer (max lenght of the list)
    def visibleSupernova(self, min_alt=30, limit_magnitude=18, date_time='now', n_values=25):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            results = []
            
            for row in c.execute('SELECT name, date, m, host, ra, dec FROM sn where m<? ORDER BY m ASC, date DESC, m ASC', (limit_magnitude)):
                # CheckVisibility
                if self.check_visibility(row[4] , row[5], min_alt):
                    results.append(row[0] + " (date: " + row[1] + ", m: " +  row[2]  + ", host: " +  row[3] + ", ra: " +  row[4]  + ", dec: " +  row[5] + ")")
            
              # Just be sure any changes have been committed or they will be lost.
            conn.close()
        
            return(results)
            
        except ValueError:
             logger.error("Error")

    # Checks if a given location s visible from user site
    # @args:
    #   1. ra - integer
    #   2. dec - float
    #   3. min_alt - integer (minimum altitude)
    # @return: True/False
    def check_visibility(self, ra, dec, min_alt=30):
        coords = ra + " " + dec
        sn = SkyCoord(coords, unit=(u.hour, u.deg), frame='icrs')
        print(sn)

        ##############################################################################
        # Use `astropy.coordinates.EarthLocation` to provide the location of Bear
        # Mountain and set the time to 11pm EDT on 2012 July 12:

        loc = EarthLocation(lat=self.lat*u.deg, lon=self.lon*u.deg, height=self.height*u.m)
        utcoffset = self.utcoffset*u.hour  # Eastern Daylight Time
        # YYY:MM:DD
        #time = Time('2017-3-1 4:00:00') - utcoffset
        time = Time(self.q_time) - utcoffset
       
        snaltaz = sn.transform_to(AltAz(obstime=time,location=loc))
        print("Altitude = {0.alt:.2}".format(snaltaz))
        print(snaltaz)
        print(snaltaz.alt.degree )
        if snaltaz.alt.degree > min_alt:
            return True
        else:
            return False

        # Checks if a given location s visible from user site
        # @args:
        #   1. ra - integer
        #   2. dec - float
        #   3. min_alt - integer (minimum altitude)
        # @return: True/False

    def get_altitude(self, ra, dec):
        coords = ra + " " + dec
        sn = SkyCoord(coords, unit=(u.hour, u.deg), frame='icrs')
        ##############################################################################
        # Use `astropy.coordinates.EarthLocation` to provide the location of Bear
        # Mountain and set the time to 11pm EDT on 2012 July 12:

        loc = EarthLocation(lat=self.lat * u.deg, lon=self.lon * u.deg, height=self.height * u.m)
        utcoffset = self.utcoffset * u.hour  # Eastern Daylight Time
        # YYY:MM:DD
        # time = Time('2017-3-1 4:00:00') - utcoffset

        time = Time(self.q_time) - utcoffset

        snaltaz = sn.transform_to(AltAz(obstime=time, location=loc))
        return(snaltaz.alt.degree)

    # Generates a file containing latest supernova (useful for external software such as TheSkyX)
    # @args:
    #   1. limit_magnitude - integer (limit mag)
    #   2. n_values - integer (max number of sn generated)
    def gen_latests_file(self, limit_magnitude=20, n_values=100):
        try:
            conn = sqlite3.connect(self.db)
            c = conn.cursor()
            results = []
            line =""
            f = open("Supernovas.txt","w") #opens file with name of "test.txt"
            
            for row in c.execute('SELECT name, date, m, host, ra, dec FROM sn where m<? ORDER BY date DESC limit ?', (limit_magnitude, n_values)):
                line= str(row[0]).ljust(30) + str(row[4]).ljust(15) + str(row[5]).ljust(15) + str(row[2]).ljust(5) + str(row[1]).ljust(15) + str(row[3]).ljust(30)
                print(line)
                f.write(line + "\n")
                    
            conn.close()
            f.close() 
            return(results)
            
        except ValueError:
             logger.error("Error")
             
        except KeyError:
            logger.error("KeyError")
        except TypeError as err:
            logger.error("TypeError",  err)
