from Commands import Commands
import time

class Director:

    def __init__(self):
        print("Creating new director engine...")
        self.master_host = "localhost"
        self.master_port = 3277
        self.slave_host = "localhost"
        self.slave_port = 0
        self.integration_time = 600
        self.master_single_exposure_time = 120
        self.slave_single_exposure_time = 5
        self.master_binning = 1
        self.slave_binning = 1
        self.master_burst = 0
        self.slave_burst = 0
        self.frame_type = "Light"
        self.dither_per_exposures = 1
        self.object_name = "NoName"
        self.master_number_of_exposures = round(self.integration_time / self.master_single_exposure_time)
        self.slave_number_of_exposures = round(self.integration_time / self.slave_single_exposure_time)
        self.current_master_exposures = 0
        self.master = None
        self.slave = None

    def set_node(self, node, host, port):
        if node == "master":
            self.master_host = host
            self.master_port = port
            self.master = Commands(self.master_host, self.master_port)
        if node == "slave":
            self.slave_host = host
            self.slave_port = port
            self.slave = Commands(self.slave_host, self.slave_port )

    def set_integration_time(self, integration_time):
        self.integration_time = integration_time

    def set_single_exposure_time(self, node, single_exposure_time):
        if node == "master":
            self.master_single_exposure_time = single_exposure_time
        if node == "slave":
            self.slave_single_exposure_time = single_exposure_time

    def set_binning(self, node, binning):
        if node == "master":
            self.master_binning = binning
        if node == "slave":
            self.slave_binning = binning

    def set_frame_type(self, frame_type):
        self.frame_type= frame_type

    def set_dither_per_exposures(self, dither_per_exposures):
        self.dither_per_exposures = dither_per_exposures

    def set_object_name(self, object_name):
        self.object_name = object_name

    def slew(self, ar, dec):
        print("Slewing to " + str(ar) + "/" + str(dec))


    def sync(self):
        self.master.sync()

    def autofocus(self, node):
        if node == "master":
            self.master.autofocus()
        if node == "slave":
            self.slave.autofocus()

    def start_guiding(self):
        self.master.guide()

    def start_seq(self):
        self.master_number_of_exposures = round(self.integration_time / self.master_single_exposure_time)
        self.master_burst = self.master_number_of_exposures / self.dither_per_exposures
        print("Master burst: " + str(self.master_burst))
        print("Master dither every: " + str(self.dither_per_exposures))
        print("Total master exposures: " + str(self.master_number_of_exposures))

        self.slave_burst = round((self.master_single_exposure_time * self.dither_per_exposures) / self.slave_single_exposure_time)
        print("Slave burst (dither every): " + str(self.slave_burst))
        self.slave_number_of_exposures = self.slave_burst * self.master_burst
        print("Total slave exposures: " + str(self.slave_number_of_exposures ))

        for i in range(int(self.master_burst)):
            print("Capturing...")
            self.master.capture(self.master_single_exposure_time, self.frame_type, "master__" + self.object_name, self.master_binning, self.dither_per_exposures)
            self.slave.capture(self.slave_single_exposure_time, self.frame_type, "slave__" + self.object_name, self.slave_binning, self.slave_burst)
            self.current_master_exposures += self.dither_per_exposures

            if self.current_master_exposures == self.master_burst:
                while self.slave.is_capturing():
                    print("Waiting for the end of current slave burst")
                    time.sleep(self.slave_single_exposure_time)
                    # Wait for end of slave burst

                self.master.do_dither()
                print("Dithering...")
                # Do dither

            # Wait till master burst is finished
            while self.master.is_capturing():
                print("Waiting for the end of current master burst")
                time.sleep(self.master_single_exposure_time)
