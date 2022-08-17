#!/usr/bin/python
# -*- coding: utf-8 -*- 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose

def engine_start_callback(data):
    global pose_date, engine_command
    pose_date = data
    engine_command = 1

def gripper_state_callback(data):
    global gripper_state
    gripper_state = data
    

gripper_pub = rospy.Publisher('/gripper_command', Pose, queue_size=10)
vision_start_pub = rospy.Publisher('/vision_start_command', String, queue_size=1)
rospy.Subscriber('/object_meta_info', Pose, engine_start_callback)
rospy.Subscriber('/gripper_state', String, gripper_state_callback)
rospy.init_node('grasp_engine', anonymous=True)
rate = rospy.Rate(1) # 1hz
grasp_selected = False
engine_command = 0
gripper_state = 0

while not rospy.is_shutdown():
    op_state = 0

    if grasp_selected:
        vision_start_pub.publish(1)

    if engine_command:
        # 파지추론엔진 알고리즘 작성부
        # 파지추론엔진으로 도출된 로봇팔 및 그리퍼 제어정보를 변수에 담아두기 (로봇팔:arm_pose, 그리퍼: gripper_pose)
        op_state = 1


    if op_state:
        # 로봇팔 및 그리퍼 제어 순차적으로 진행
        # 로봇팔 제어 -> arm_pose를 명령던짐
        # 그리퍼 제어 -> gripper_pub.publish(gripper_pose)
        engin_command = 0
        op_state = 0

    rospy.loginfo(gripper_state)
    rate.sleep()