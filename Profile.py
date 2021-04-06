############################################################
# -*- coding: utf-8 -*-
#
# SAAS access to CCDCiel profiles
#
# Francisco José Calvo Fernández (http://www.irydeo.com)
# (c) 2021
# Licence GPL v3
############################################################
import xml.etree.ElementTree as ET
from pathlib import Path
import glob

#
class Profile:
    def __init__(self):
        print("Creating new profiles engine...")
        self.base_url = str(Path.home()) +  "/.config/ccdciel/"

    def get_port(self, profile):
        url = self.base_url + "ccdciel_" + profile + ".conf" # Only Linux
        tree = ET.parse(url)
        root = tree.getroot()
        return root.findall(".//Files[1]")[0].attrib['TCPIPConfigPort']

    def get_list(self):
        profiles = []
        for name in glob.glob(self.base_url + 'ccdciel_*.conf'):
            name = name.replace(self.base_url + "ccdciel_", "").replace(".conf", "")
            profiles.append(name)
        return profiles