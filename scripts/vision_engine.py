#!/usr/bin/python
# -*- coding: utf-8 -*- 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose
import numpy as np
 
def vision_start_callback(data):
    global vision_command
    vision_command = data


pub = rospy.Publisher('/object_meta_info', Pose, queue_size=10)
rospy.Subscriber('/vision_start_command', String, vision_start_callback)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(0.2) # 0.2hz
p = Pose()
vision_command = 0

while not rospy.is_shutdown():
    if vision_command:
        # 비전 알고리즘 작성부
        # 물체 자세추정 정보를 p에 담기

        pub.publish(p)
        vision_command = 0
    rospy.loginfo('test printing_vision_engine')
    rate.sleep()