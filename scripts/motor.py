#!/usr/bin/env python
#motor 0 (servo C) it controls the direction of the wheels

import RPi.GPIO as GPIO

# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

#Motor_B_EN    = 4
#Motor_B_Pin1  = 26
#Motor_B_Pin2  = 21
#pwn_B = 0

Motor_A_EN    = 17
Motor_A_Pin1  = 27
Motor_A_Pin2  = 18
pwm_A = 0


def motorStop():#Motor stops
  GPIO.output(Motor_A_Pin1, GPIO.LOW)           # type: ignore
  GPIO.output(Motor_A_Pin2, GPIO.LOW)           # type: ignore
  GPIO.output(Motor_A_EN, GPIO.LOW)             # type: ignore


def setup():#Motor initialization
  global pwm_A
  GPIO.setwarnings(False)                       # type: ignore
  GPIO.setmode(GPIO.BCM)                        # type: ignore
  GPIO.setup(Motor_A_EN, GPIO.OUT)              # type: ignore
  GPIO.setup(Motor_A_Pin1, GPIO.OUT)            # type: ignore
  GPIO.setup(Motor_A_Pin2, GPIO.OUT)            # type: ignore

  motorStop()
  try:
    pwm_A = GPIO.PWM(Motor_A_EN, 1000)          # type: ignore
  except:
    pass


def motor_A(status, speed):      # Motor A positive and negative rotation.
  if status == 0: # stop
    GPIO.output(Motor_A_Pin1, GPIO.LOW)         # type: ignore
    GPIO.output(Motor_A_Pin2, GPIO.LOW)         # type: ignore
    GPIO.output(Motor_A_EN, GPIO.LOW)           # type: ignore
  elif status == 1:              # positive rotation.
      GPIO.output(Motor_A_Pin1, GPIO.LOW)       # type: ignore
      GPIO.output(Motor_A_Pin2, GPIO.HIGH)      # type: ignore
      pwm_A.start(100)                          # type: ignore
      pwm_A.ChangeDutyCycle(speed)              # type: ignore
  elif status == -1:             # negative rotation.
      GPIO.output(Motor_A_Pin1, GPIO.HIGH)      # type: ignore
      GPIO.output(Motor_A_Pin2, GPIO.LOW)       # type: ignore
      pwm_A.start(0)                            # type: ignore
      pwm_A.ChangeDutyCycle(speed)              # type: ignore
      

def move(speed, direction): 
  #speed = 100
  if direction == 'forward':
      motor_A(1, speed)
  elif direction == 'backward':
      motor_A(-1, speed)
  elif direction == 'stop':
      motor_A(0, speed)
  else:
    pass

def destroy():
  motorStop()
  GPIO.cleanup()             # Release resource # type: ignore
