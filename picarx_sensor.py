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
    
class PicarXSensor():
    
    def __init__(self):
        
        self.S0 = ADC('A0')
        self.S1 = ADC('A1')
        self.S2 = ADC('A2')    
    
    
    def read_sensors(self):
        
        adc_value_list = []
        adc_value_list.append(self.S0.read())
        adc_value_list.append(self.S1.read())
        adc_value_list.append(self.S2.read())
        return adc_value_list
    