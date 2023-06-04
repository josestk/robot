#!/usr/bin/env python

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(10)


servo_A_straight = 390
servo_A_Right = 290
servo_A_Left = 500

servo_B_straight = 380
servo_B_Right = 290
servo_B_Left = 500

servo_C_straight = 400
servo_C_Up = 500
servo_C_Down = 350

servo_A = 0   # PWM port number.
servo_B = 1   # PWM port number.
servo_C = 2   # PWM port number.

# Set the value of PWM to control rotation.
def servo_value(servo, value):  # The value range is between 100-500.
    pwm.set_pwm(servo, 0, value)
    

def init():
    pwm.set_pwm(servo_A, 0, servo_A_straight)  
    pwm.set_pwm(servo_B, 0, servo_B_straight)
    pwm.set_pwm(servo_C, 0, servo_C_straight)
