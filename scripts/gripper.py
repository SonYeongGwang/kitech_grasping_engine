#!/usr/bin/python
# -*- coding: utf-8 -*- 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose

def gripper_command_callback(data):
    global gripper_pose, gripper_command
    gripper_pose = data
    gripper_command = 1
    

rospy.Subscriber("gripper_command", Pose, gripper_command_callback)
rospy.init_node('listener', anonymous=True)
rate = rospy.Rate(1) # 1hz

gripper_command = 0

while not rospy.is_shutdown():
    if gripper_command:
        # 그리퍼 구동 알고리즘 작성부
        gripper_command = 0

    rospy.loginfo('test printing_gripper')
    rate.sleep()