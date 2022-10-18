#!/usr/bin/python
# -*- coding: utf-8 -*- 

import rospy
from std_msgs.msg import String
from kitech_grasping_engine.msg import FingerState, SuctionState, GripperState
import numpy as np
 
gripper_state_pub = rospy.Publisher('/gripper_state', GripperState, queue_size=10)
rospy.init_node('state_talker', anonymous=True)
rate = rospy.Rate(5) # 1Hz
fs = FingerState()
ss = SuctionState()
gs = GripperState()
while not rospy.is_shutdown():
    # 그리퍼 상태 알림 알고리즘 작성부

    fs.stroke = 0.01
    fs.torque = 0.5

    ss.stroke = 0.008
    ss.angle = 0.1

    gs.finger = fs
    gs.suction = ss

    gripper_state_pub.publish(gs)
    rate.sleep()