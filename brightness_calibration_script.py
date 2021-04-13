#!/usr/bin/env python3

from picarx_sensor import PicarXSensor
from picarx_interpreter import PicarXInterpreter
import numpy as np


def gather_data(sensor):
    sum_of_readings = np.array([0,0,0]);
    for i in range(0,10):
        new_reading = np.array(car_sensor.read_sensors())
        sum_of_readings += new_reading
    average_reading = sum_of_readings/10
    return average_reading.tolist()

car_sensor = PicarXSensor()
sensor_interpreter = PicarXInterpreter()

print("Please place the inside of the left wheel on the left edge of the line.")
print("Press enter when ready")
input()
av_read = gather_data(car_sensor)
print("Average sensor reading is: {}".format(av_read))
print("Interpreter returned {} for a brightness of 0.5".format(sensor_interpreter.process_reading(av_read)))

print("Please place the center of the car over the center of the line.")
print("Press enter when ready")
input()
av_read = gather_data(car_sensor)
print("Average sensor reading is: {}".format(av_read))
print("Interpreter returned {} for a brightness of 0.5".format(sensor_interpreter.process_reading(av_read)))



print("Please place the inside of the right wheel on the right edge of the line.")
print("Press enter when ready")
input()
av_read = gather_data(car_sensor)
print("Average sensor reading is: {}".format(av_read))
print("Interpreter returned {} for a brightness of 0.5".format(sensor_interpreter.process_reading(av_read)))
