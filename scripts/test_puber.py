#!/usr/bin/python

import rospy
from geometry_msgs.msg import Pose
import numpy as np
 
pub = rospy.Publisher('/object_meta_info', Pose, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(0.2) # 10hz
p = Pose()

while not rospy.is_shutdown():
    p.position.x = 1
    p.position.y = 2
    p.position.z = 3
    p.orientation.x = 1
    p.orientation.y = 1
    p.orientation.z = 1
    p.orientation.w = 0.5
    rospy.loginfo(p)
    pub.publish(p)
    rate.sleep()