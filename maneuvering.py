#!/usr/bin/env python3

import sys
sys.path.append(r'/home/pi/RobotSystems/')
from picarx_improved import *

def go_forward(theta):
  set_dir_servo_angle(theta)
  forward(50)
  delay(2000)
  stop()
  
def go_back(theta):
  set_dir_servo_angle(theta)
  backward(50)
  delay(2000)
  stop()
  
def pp_left():
  set_dir_servo_angle(0)
  forward(50)
  delay(500)
  set_dir_servo_angle(-30)
  forward(50)
  delay(500)
  set_dir_servo_angle(0)
  forward(50)
  delay(500)
  set_dir_servo_angle(30)
  forward(50)
  delay(500)
  set_dir_servo_angle(0)
  forward(50)
  delay(500)
  backward(50)
  delay(250)
  set_dir_servo_angle(-15)
  forward(50)
  delay(250)
  set_dir_servo_angle(0)
  backward(50)
  delay(250)
  
  stop()
  
def pp_right():
  set_dir_servo_angle(0)
  forward(50)
  delay(500)
  set_dir_servo_angle(30)
  forward(50)
  delay(500)
  set_dir_servo_angle(0)
  forward(50)
  delay(500)
  set_dir_servo_angle(-30)
  forward(50)
  delay(500)
  set_dir_servo_angle(0)
  forward(50)
  delay(500)
  backward(50)
  delay(250)
  set_dir_servo_angle(15)
  forward(50)
  delay(250)
  set_dir_servo_angle(0)
  backward(50)
  delay(250)
  
  stop()
  
def kturn_left():
  set_dir_servo_angle(-45)
  forward(50)
  delay(1000)
  set_dir_servo_angle(45)
  backward(50)
  delay(1000)
  set_dir_servo_angle(0)
  forward(50)
  delay(2000)
  stop()
  
def kturn_right():
  set_dir_servo_angle(45)
  forward(50)
  delay(1000)
  set_dir_servo_angle(-45)
  backward(50)
  delay(1000)
  set_dir_servo_angle(0)
  forward(50)
  delay(2000)
  stop()

if __name__ == "__main__":
  user_exit = 0
  while not user_exit:
    print("Please choose from the following:")
    print(" '1': forward - '2': back - '3': parallel park - '4': k turn - 'q': quit")
    action = input()
    if action == "1":
      print("Please enter a steering angle from -90 degrees to 90 degrees.")
      steering_angle = input()
      go_forward(int(steering_angle))
    if action == "2":
      print("Please enter a steering angle from -90 degrees to 90 degrees.")
      steering_angle = input()
      go_back(int(steering_angle))
    if action == "3":
      print("Please choose a direction 'left' or 'right' for this maneuver")
      turn_dir = input()
      if turn_dir == "left":
        pp_left()
      elif turn_dir == "right":
        pp_right
      else:
        print("Input was invalid. Please type either 'left' or 'right'")
    if action == "4":
      print("Please choose a direction 'left' or 'right' for this maneuver")
      turn_dir = input()
      if turn_dir == "left":
        kturn_left()
      elif turn_dir == "right":
        kturn_right
      else:
        print("Input was invalid. Please type either 'left' or 'right'")
    if action == "q":
      user_exit = 1
      
  
