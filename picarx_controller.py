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
    
from picarx_improved_class import Picar_X

class PicarXController():
    
    def __init__(self, kp=100):
        self.kp = kp
        self.car = Picar_X()
    
    def steer_car(self, error):
        angle = self.kp*error
        self.car.set_dir_servo_angle(angle)
        return angle