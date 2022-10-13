#!/home/vision/.virtualenvs/torch_env/bin/python
# -*- coding: utf-8 -*- 

import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import Pose
from kitech_grasping_engine.msg import MultiPoseInfo ,SinglePoseInfo
import numpy as np

import yaml
import os
import glob
 
home_path = os.path.expanduser('~')

# def vision_start_callback(data):
#     global vision_command
#     vision_command = data

pub = rospy.Publisher('/object_meta_info', MultiPoseInfo, queue_size=10)
# rospy.Subscriber('/vision_start_command', Int16, vision_start_callback)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(0.2) # 0.2hz

object_detected = 3

# m_pose_info = MultiPoseInfo()

pose_set = {}
while not rospy.is_shutdown():
    res = glob.glob(home_path+'/catkin_ws/start*')
    if len(res) > 0:
        # 비전 알고리즘 작성부

        for i in range(object_detected):
            pose_set[str(i)] = {}
            pose_set[str(i)]['shape'] = int(np.random.randint(0, 2, (1, ))[0])
            pose_set[str(i)]['shape_para'] = [1, 2, 3, 4]
            pose_set[str(i)]['position'] = [1, 2, 3]
            pose_set[str(i)]['orientation'] = [1, 0, 0, 0]

            # pose_info = SinglePoseInfo()
            # pose_info.shape = i
            # pose_info.shape_parameters = [1, 2, 3, 4]
            # pose_set.append(pose_info)

        # m_pose_info = pose_set

        rospy.loginfo("pose_set")
        print(pose_set)

        with open(home_path+'/catkin_ws/pose_information.yaml', 'w') as f:
            yaml.dump(pose_set, f, default_flow_style=None)

        # pub.publish(m_pose_info)
        os.system('rm '+res[0])
    rospy.loginfo('test printing_vision_engine')
    # rospy.loginfo(m_pose_info)
    rate.sleep()