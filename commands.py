############################################################
# -*- coding: utf-8 -*-
#
# SAAS <-> CCDCiel communication
#
# Francisco José Calvo Fernández (http://www.irydeo.com)
# (c) 2021
# Licence GPL v3
############################################################

from ccdciel import ccdciel
from astropy import units as u
from astropy.coordinates import SkyCoord
import os


class Commands:

    def __init__(self, host="localhost", port="3277"):
        self.phost= str(host)
        self.pport = str(port)
        self.debug = 0
        self.simulator_number_of_calls = 0

    def set_self_url(self):
        os.environ['CCDCIEL_HOST'] = self.phost
        os.environ['CCDCIEL_PORT'] = self.pport

    def capture(self, exposure, frametype='Light', objectname='NoName', binning=1, count = 1, dither=0):

        if not self.debug:
            self.set_self_url()
            ccdciel('Capture_setexposure', exposure)['result']
            ccdciel('Capture_setframetype', frametype)['result']
            ccdciel('Capture_setobjectname', objectname)['result']
            ccdciel('Capture_setcount', count)['result']
            ccdciel('Capture_setbinning', binning)['result']
            if dither != 0:
                ccdciel('Capture_setdither', dither)['result']
            ccdciel('Capture_start')['result']
        else:
            print("DEBUG CMD: Capture_start")

    def guide(self):

        if not self.debug:
            self.set_self_url()
            ccdciel('Autoguider_startguiding')['result']
        else:
            print("DEBUG CMD: Autoguider_startguiding")

    def stop_guide(self):

        if not self.debug:
            self.set_self_url()
            ccdciel('Autoguider_stopguiding')['result']
        else:
            print("DEBUG CMD: Autoguider_startguiding")

    def slew(self, ra, dec):
        self.set_self_url()
        print(self.phost)
        print(self.pport)
        # Transform coords
        c = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))
        ccdciel('Telescope_slewasync', [c.ra.hour, c.dec.degree])['result']


    def sync(self):
        self.set_self_url()
        ccdciel('Astrometry_sync')['result']

    def autofocus(self):
        self.set_self_url()
        ccdciel('Autofocus')['result']

    def is_capturing(self):
        if not self.debug:
            self.set_self_url()
            result = ccdciel('Capture_running')['result']
            if bool(result): # Check if empty
                return result
            else:
                return False
        else:
            print("DEBUG CMD: Capture_running")
            self.simulator_number_of_calls += 1
            if self.simulator_number_of_calls > 10:
                return 0
            else:
                return 1

    def is_slewing(self):
        if not self.debug:
            self.set_self_url()
            return ccdciel('Telescope_slewing')['result']
        else:
            print("DEBUG CMD: Telescope_slewing")
            return 0

    def is_guiding(self):
        if not self.debug:
            self.set_self_url()
            return ccdciel('Autoguider_guiding')['result']
        else:
            print("DEBUG CMD: Guiding")
            return 0

    def do_dither(self):
        if not self.debug:
            self.set_self_url()  # Send message in the self node
            ccdciel('Autoguider_dither')['result']
        else:
            print("DEBUG CMD: Dither_running")

    def wheel_setfilter(self, number):
        self.set_self_url()
        ccdciel('Wheel_setfilter', number)['result']
