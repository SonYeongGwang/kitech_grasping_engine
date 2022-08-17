#!/usr/bin/python
# -*- coding: utf-8 -*- 

import rospy
from std_msgs.msg import String
import numpy as np
 
pub = rospy.Publisher('/gripper_state', String, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1) # 1Hz

while not rospy.is_shutdown():
    # 그리퍼 상태 알림 알고리즘 작성부
    hello_str = "State: NORMAL %s" % rospy.get_time()
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()