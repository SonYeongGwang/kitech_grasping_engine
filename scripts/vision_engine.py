#!/usr/bin/python
# -*- coding: utf-8 -*- 

import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import Pose
from kitech_grasping_engine.msg import MultiPoseInfo ,SinglePoseInfo
import numpy as np
 
def vision_start_callback(data):
    global vision_command
    vision_command = data

pub = rospy.Publisher('/object_meta_info', MultiPoseInfo, queue_size=10)
rospy.Subscriber('/vision_start_command', Int16, vision_start_callback)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(0.2) # 0.2hz
vision_command = 0

object_detected = 3

pose_set = []
m_pose_info = MultiPoseInfo()

while not rospy.is_shutdown():
    if vision_command:
        # 비전 알고리즘 작성부
        # 물체 자세추정 정보를 p에 담기

        for i in range(object_detected):
            pose_info = SinglePoseInfo()
            pose_info.shape = i
            pose_info.shape_parameters = [1, 2, 3, 4]
            pose_set.append(pose_info)

        m_pose_info = pose_set

        pub.publish(m_pose_info)
        vision_command = 0
    rospy.loginfo('test printing_vision_engine')
    rospy.loginfo(m_pose_info)
    rate.sleep()