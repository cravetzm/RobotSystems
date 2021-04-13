#!/usr/bin/env python3

import sys
sys.path.append(r'/home/pi/RobotSystems/')
from picarx_improved import *

set_dir_servo_angle(0)
forward(50)
delay(5000)