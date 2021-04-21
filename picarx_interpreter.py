#!/usr/bin/env python3

try:
    from  ezblock  import *
    #__reset_mcu__()
    #time.sleep (0.01)
except  ImportError:
    print ("This  computer  does  not  appear  to be a PiCar -X system \
           (/opt/ezblock  is not  present). Shadowing  hardware  calls \
            with  substitute  functions ")
    from  sim_ezblock  import *
import numpy as np
    
class PicarXInterpreter():
    
    def __init__(self, brightness=0.5, polarity = 1):
        #brightness is 0 for a totaly dark room and 1 for perfect vision
        self.brightness = brightness
        #polarity is 1 for a bright line on dark surface and -1 for a dark line on a bright surface
        self.polarity  = polarity
        
    def process_reading(self, reading):
        #find the difference between adjacent readings
        sensor_grad = np.diff(np.array(reading)/1024) #[line to right skew, line to left skew] if polarity is 1
        total_skew = self.polarity * sum(sensor_grad)
        #adjust for brightness (brightness is 0 to 1, so divide to boost low contrast)
        adjusted_total_skew = total_skew / self.brightness
        #cap the value from -1 to 1 (todo: tune well enough that this is not needed)
        control_error = max(min(adjusted_total_skew, 1), -1)
        return control_error