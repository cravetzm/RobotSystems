#!/usr/bin/env python3

from picarx_sensor import PicarXSensor
from picarx_interpreter import PicarXInterpreter
from picarx_controller import PicarXController

car_sensor = PicarXSensor()
sensor_interpreter = PicarXInterpreter(brightness = 0.3, polarity = -1)
car_controller = PicarXController()

def follow():
  reading = car_sensor.read_sensors()
  line_error = sensor_interpreter.process_reading(reading)
  _ = car_controller.steer_car(line_error)
  
if __name__ == "__main__":
  while True:
    follow()
    car_controller.car.forward(30)