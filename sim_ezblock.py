# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:22:36 2021

@author: Miranda
"""
import sys
sys.path.append("D:/Documents/OSU Classes/RobotSystems/ezblock") 
from basic import _Basic_class
#from i2c import I2C


class Servo(_Basic_class):
    MAX_PW = 2500
    MIN_PW = 500
    _freq = 50
    
    def __init__(self, pwm):
        self.pwm = pwm
        super().__init__()

    # angle ranges -90 to 90 degrees
    def angle(self, angle):
        pass
    
class PWM():

    def __init__(self, channel, debug="critical"):
        super().__init__()
        
    def i2c_write(self, reg, value):
        pass

    def freq(self, *freq):
        return 0

    def prescaler(self, *prescaler):
        return 0

    def period(self, *arr):
        pass

    def pulse_width(self, *pulse_width):
        return 0

    def pulse_width_percent(self, *pulse_width_percent):
        return 0


class Pin(_Basic_class):


    def __init__(self, *value):
        super().__init__()
        
    def check_board_type(self):
        pass

    def init(self, mode, pull=0):
        pass
    
    def dict(self, *_dict):
        return {}

    def __call__(self, value):
        return 0

    def value(self, *value):
        return 0

    def on(self):
        return 0

    def off(self):
        return 0

    def high(self):
        return 0

    def low(self):
        return 0

    def mode(self, *value):
        return(0,0)

    def pull(self, *value):
        return 0

    def irq(self, handler=None, trigger=None, bouncetime=200):
        pass

    def name(self):
        return ""

    def names(self):
        return ["", ""]
    
class ADC():

    def __init__(self, chn):    # 参数，通道数，树莓派扩展板上有8个adc通道分别为"A0, A1, A2, A3, A4, A5, A6, A7"
        super().__init__()

        
    def read(self):                     # adc通道读取数---写一次数据，读取两次数据 （读取的数据范围是0~4095）
        return 0

    def read_voltage(self):                             # 将读取的数据转化为电压值（0~3.3V）
        return 0