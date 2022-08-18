#!/usr/bin/python
# -*- coding: utf-8 -*- 

import rospy
from std_msgs.msg import String
from kitech_grasping_engine.msg import FingerState, SuctionState
import numpy as np
 
finger_pub = rospy.Publisher('/finger_state', FingerState, queue_size=10)
suction_pub = rospy.Publisher('/suction_state', SuctionState, queue_size=10)
rospy.init_node('state_talker', anonymous=True)
rate = rospy.Rate(1) # 1Hz
fs = FingerState()
ss = SuctionState()
while not rospy.is_shutdown():
    # 그리퍼 상태 알림 알고리즘 작성부

    fs.current_stroke = 1
    fs.current_torque = 1
    fs.goal_stroke = 1
    fs.goal_torque = 1

    ss.current_stroke = 1
    ss.goal_stroke = 1
    ss.current_angle = 1
    ss.goal_angle = 1

    finger_pub.publish(fs)
    suction_pub.publish(ss)
    rate.sleep()