#!/usr/bin/env python3
import time
try:
    from  ezblock  import *
    #__reset_mcu__()
    #time.sleep (0.01)
except  ImportError:
    print ("This  computer  does  not  appear  to be a PiCar -X system \
           (/opt/ezblock  is not  present). Shadowing  hardware  calls \
            with  substitute  functions ")
    from  sim_ezblock  import *
import atexit
import math

PERIOD = 4095
PRESCALER = 10
TIMEOUT = 0.02

dir_servo_pin = Servo(PWM('P2'))
camera_servo_pin1 = Servo(PWM('P0'))
camera_servo_pin2 = Servo(PWM('P1'))
left_rear_pwm_pin = PWM("P13")
right_rear_pwm_pin = PWM("P12")
left_rear_dir_pin = Pin("D4")
right_rear_dir_pin = Pin("D5")

S0 = ADC('A0')
S1 = ADC('A1')
S2 = ADC('A2')

Servo_dir_flag = 1
#MC edited 4/8: car pulls ~14 degrees to the left naaturally
dir_cal_value = 14
cam_cal_value_1 = 0
cam_cal_value_2 = 0
motor_direction_pins = [left_rear_dir_pin, right_rear_dir_pin]
motor_speed_pins = [left_rear_pwm_pin, right_rear_pwm_pin]
cali_dir_value = [1, -1]
cali_speed_value = [0, 0]
#初始化PWM引脚

#MC edited 4/8: make the current steering angle known
dir_curr_value = dir_cal_value

for pin in motor_speed_pins:
    pin.period(PERIOD)
    pin.prescaler(PRESCALER)

def set_motor_speed(motor, speed):
    global cali_speed_value,cali_dir_value
    motor -= 1
    if speed >= 0:
        direction = 1 * cali_dir_value[motor]
    elif speed < 0:
        direction = -1 * cali_dir_value[motor]
    #MC edited on 4/8 to remove speed scaling but keep requirement that speed is an integer
    speed = int(abs(speed))
    speed = speed - cali_speed_value[motor]
    if direction < 0:
        motor_direction_pins[motor].high()
        motor_speed_pins[motor].pulse_width_percent(speed)
    else:
        motor_direction_pins[motor].low()
        motor_speed_pins[motor].pulse_width_percent(speed)

def motor_speed_calibration(value):
    global cali_speed_value,cali_dir_value
    cali_speed_value = value
    if value < 0:
        cali_speed_value[0] = 0
        cali_speed_value[1] = abs(cali_speed_value)
    else:
        cali_speed_value[0] = abs(cali_speed_value)
        cali_speed_value[1] = 0

def motor_direction_calibration(motor, value):
    # 0: positive direction
    # 1:negative direction
    global cali_dir_value
    motor -= 1
    if value == 1:
        cali_dir_value[motor] = -1*cali_dir_value[motor]


def dir_servo_angle_calibration(value):
    global dir_cal_value
    dir_cal_value = value
    set_dir_servo_angle(dir_cal_value)
    # dir_servo_pin.angle(dir_cal_value)

#MC edited 4/8: update the current steering angle
def set_dir_servo_angle(value):
    global dir_cal_value
    global dir_curr_value 
    dir_curr_value= value
    dir_servo_pin.angle(dir_curr_value+dir_cal_value)

def camera_servo1_angle_calibration(value):
    global cam_cal_value_1
    cam_cal_value_1 = value
    set_camera_servo1_angle(cam_cal_value_1)
    # camera_servo_pin1.angle(cam_cal_value)

def camera_servo2_angle_calibration(value):
    global cam_cal_value_2
    cam_cal_value_2 = value
    set_camera_servo2_angle(cam_cal_value_2)
    # camera_servo_pin2.angle(cam_cal_value)

def set_camera_servo1_angle(value):
    global cam_cal_value_1
    camera_servo_pin1.angle(-1 *(value+cam_cal_value_1))

def set_camera_servo2_angle(value):
    global cam_cal_value_2
    camera_servo_pin2.angle(-1 * (value+cam_cal_value_2))

def get_adc_value():
    adc_value_list = []
    adc_value_list.append(S0.read())
    adc_value_list.append(S1.read())
    adc_value_list.append(S2.read())
    return adc_value_list

def set_power(speed):
    set_motor_speed(1, speed)
    set_motor_speed(2, speed) 

#MC edited 4/8 to account for turns
def backward(speed):
    global dir_curr_value 
    rad = math.pi*dir_curr_value / 180
    speed_diff = 0.5625*abs(math.tan(rad))
    inside_speed = speed * (1 - speed_diff)
    outside_speed = speed * (1 + speed_diff)
    if (dir_curr_value >= 0):
      set_motor_speed(1, outside_speed)
      set_motor_speed(2, inside_speed)
    else:
      set_motor_speed(1, inside_speed)
      set_motor_speed(2, outside_speed)

#MC edited 4/8 to account for turns
def forward(speed):
    global dir_curr_value 
    rad = math.pi*abs(dir_curr_value) / 180
    speed_diff = 0.5625*math.tan(rad)
    inside_speed = speed * (1 - speed_diff)
    outside_speed = speed * (1 + speed_diff)
    if (dir_curr_value >= 0):
      set_motor_speed(1, -1*inside_speed)
      set_motor_speed(2, -1*outside_speed)
    else:
      set_motor_speed(1, -1*outside_speed)
      set_motor_speed(2, -1*inside_speed)

def stop():
    set_motor_speed(1, 0)
    set_motor_speed(2, 0)


def Get_distance():
    timeout=0.01
    trig = Pin('D8')
    echo = Pin('D9')

    trig.low()
    time.sleep(0.01)
    trig.high()
    time.sleep(0.000015)
    trig.low()
    pulse_end = 0
    pulse_start = 0
    timeout_start = time.time()
    while echo.value()==0:
        pulse_start = time.time()
        if pulse_start - timeout_start > timeout:
            return -1
    while echo.value()==1:
        pulse_end = time.time()
        if pulse_end - timeout_start > timeout:
            return -2
    during = pulse_end - pulse_start
    cm = round(during * 340 / 2 * 100, 2)
    #print(cm)
    return cm
     
def test():
    # dir_servo_angle_calibration(-10) 
    set_dir_servo_angle(-40)
    # time.sleep(1)
    # set_dir_servo_angle(0)
    # time.sleep(1)
    # set_motor_speed(1, 1)
    # set_motor_speed(2, 1)
    # camera_servo_pin.angle(0)


#MC added this on 4-8 to stop the motors from running after a program terminates    
atexit.register(stop)
