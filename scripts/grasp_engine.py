#!/usr/bin/python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose

def engine_start_callback(data):
    '''
    Callback that starts grasp engine when the output from vision algorithm has arrived to this node.
    The loop speed of this callback is dependent to the vision loop because of the flag `grasp_selected`
    When `grasp_selected = True`, this node will publish selected grasp configuration once.

    Argument:
        data (geometry_msgs.msg): msg which contains `position`, `orientation`, `shape`, `parameters`

    Examples::

        >>> data.position       # when accessing to the position data
        >>> data.orientation    # when accessing to the orientation data
    '''
    global grasp_selected, output_from_engine, gripper_state

    ## <<< insert grasp engine here >>>
    rospy.loginfo('task inside grasping engine...')
    rospy.loginfo('gripper state: {}'.format(gripper_state))
    output_from_engine = [1, 1, 1, 1, 1, 1, 1]
    ## <<< insert grasp engine here >>>

    ''' 'grasp_selected = False' if the algorithm fails to find feasible grasp configuration'''
    # feasible_grasp = False
    feasible_grasp = True

    if feasible_grasp:
        grasp_selected = True
    else:
        pass

def gripper_state_callback(data):
    '''
    Callback that acquires gripper states when the gripper sends its states to this node.
    The loop speed of this callback is dependent to the gripper loop.

    Argument:
        data (geometry_msgs.msg): msg which contains `position`, `orientation`, `initalized`, `length`, ...

    Examples::

        >>> data.position       # when accessing to the position data
        >>> data.orientation    # when accessing to the orientation data
    '''
    global gripper_state

    gripper_state = data.data
    rospy.loginfo(gripper_state)
    

grasp_selected = False
gripper_pub = rospy.Publisher('/gripper_command', Pose, queue_size=10)
vision_start_command = rospy.Publisher('/vision_start_command', String, queue_size=1)
rospy.Subscriber('/object_meta_info', Pose, engine_start_callback)
rospy.Subscriber('/gripper_state', String, gripper_state_callback)
rospy.init_node('grasp_engine', anonymous=True)
rate = rospy.Rate(10) # 10hz
gripper_pose = Pose()

while not rospy.is_shutdown():

    if grasp_selected:
        gripper_pose.position.x = output_from_engine[0]
        gripper_pose.position.y = output_from_engine[1]
        gripper_pose.position.z = output_from_engine[2]
        gripper_pose.orientation.x = output_from_engine[0]
        gripper_pose.orientation.y = output_from_engine[1]
        gripper_pose.orientation.z = output_from_engine[2]
        gripper_pose.orientation.w = output_from_engine[3]

        rospy.loginfo(gripper_pose)
        gripper_pub.publish(gripper_pose)
        grasp_selected = False
    else:
        pass

    rate.sleep()
