#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import sshkeyboard

def publisher(key):
    
    rospy.loginfo(key)
    pub.publish(key)



if __name__ == '__main__': #funcion principal

  try:
    
    pub = rospy.Publisher('keyboard_input', String,queue_size=10)
    rospy.init_node('keyboard_scanner',anonymous=True)

    sshkeyboard.listen_keyboard(on_press=publisher)
    
  except rospy.ROSInterruptException:
    pass