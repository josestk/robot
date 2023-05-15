#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String

import motor
import servos
import leds

motor_speed = 100

def move(key): #movimiento del robot
  
  print(key.data)
  if key.data == 'w':
    motor.move(motor_speed, 'forward')
  elif key.data == 's':
    motor.move(motor_speed, 'backward')
  elif key.data == 'a':
    servos.servo_value(servos.servo_A, servos.servo_A_Left)  
  elif key.data == 'd':
    servos.servo_value(servos.servo_A, servos.servo_A_Right)  
  elif key.data == 'space':
    motor.motorStop()
    servos.init()
  elif key.data == 'left':
    servos.servo_value(servos.servo_B, servos.servo_B_straight)
    servos.servo_value(servos.servo_B, servos.servo_B_Left)
  elif key.data == 'right':
    servos.servo_value(servos.servo_B, servos.servo_B_straight)
    servos.servo_value(servos.servo_B, servos.servo_B_Right)
  elif key.data == 'up':
    servos.servo_value(servos.servo_C, servos.servo_C_Up)
  elif key.data == 'down':
    servos.servo_value(servos.servo_C, servos.servo_C_Down)


def listener():

  rospy.init_node('listener',anonymous=True)
  rospy.Subscriber('keyboard_input',String,move)

  rospy.spin()


def init(): #inicializa todos los componentes necesarios

  servos.init()
  motor.setup()


if __name__ == '__main__': #funcion principal

  init()
  try:
    listener()

    leds.led = LED()
    leds.led.colorWipe(255,255,255)
  except rospy.ROSInterruptException:
    pass


  