#!/usr/bin/env python3

from picarx_sensor import PicarXSensor
from picarx_interpreter import PicarXInterpreter
import numpy as np

safety_factor = 0.8

def gather_data(sensor):
    sum_of_readings = np.array([0,0,0]);
    for i in range(0,10):
        new_reading = np.array(car_sensor.read_sensors())
        sum_of_readings += new_reading
    average_reading = sum_of_readings/10
    return average_reading.tolist()

car_sensor = PicarXSensor()
sensor_interpreter = PicarXInterpreter(brightness = 0.5, polarity = -1)
errors = []

print("Please place the left edge of the sensor array over the left edge of the line.")
print("Press enter when ready")
input()
av_read = gather_data(car_sensor)
print("Average sensor reading is: {}".format(av_read))
errors.append(sensor_interpreter.process_reading(av_read))
print("Interpreter returned {} for a brightness of 0.5".format(errors[0]))

print("Please place the center of the car over the center of the line.")
print("Press enter when ready")
input()
av_read = gather_data(car_sensor)
print("Average sensor reading is: {}".format(av_read))
errors.append(sensor_interpreter.process_reading(av_read))
print("Interpreter returned {} for a brightness of 0.5".format(errors[1]))



print("Please place the right edge of the sensor array over the right edge of the line.")
print("Press enter when ready")
input()
av_read = gather_data(car_sensor)
print("Average sensor reading is: {}".format(av_read))
errors.append(sensor_interpreter.process_reading(av_read))
print("Interpreter returned {} for a brightness of 0.5".format(errors[2]))

print("Suggested brightness is {}.".format(max(errors)*0.5/safety_factor))
