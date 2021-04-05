#  This script unpark the telescope mount

from Director import Director

director = Director()
director.set_node("master", "localhost", 3277)
director.set_node("slave", "localhost", 47089)
director.set_integration_time(60) # Set total integration time in seconds
director.set_single_exposure_time("master", 15)    # Master exposures are 120s
director.set_single_exposure_time("slave", 5)    # Master exposures are 120s
director.set_binning("master", 1)
director.set_binning("slave", 1)
director.set_frame_type("Light")

director.set_dither_per_exposures(1) # Dither each frame in master node, system will calculate needed data for slave

# Rest of exposure data:
director.set_object_name("myObject") #it will be master_myObject and slave_myObject

director.slew(10.5, 45.7)
director.sync()
director.autofocus("master")
director.autofocus("slave")
director.start_guiding()
director.start_seq() # It will launch each node, stop when needed...



