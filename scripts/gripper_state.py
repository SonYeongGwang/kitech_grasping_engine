#!/usr/bin/python

import rospy
from std_msgs.msg import String
import numpy as np
 
pub = rospy.Publisher('/gripper_state', String, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) # 100hz

while not rospy.is_shutdown():
    hello_str = "State: NORMAL %s" % rospy.get_time()
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()