#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

time = 0
def timer(msg):
    global time
    
    # increase time
    time += msg.data

    # print time
    rospy.loginfo('Timer: {}'.format(time))


def time_reset(msg):
    global time

    if msg.data == True:
        time = 0
        
        return True, 'Time was reseted.'

    else:
        return False, 'Time was not reseted.'

if __name__ == '__main__':

    # initiate node
    rospy.init_node('time_with_reset_node')

    # create a subscriber
    rospy.Subscriber(name='/one_second_signal', data_class=Int64, callback=timer)

    # create service
    rospy.Service(name='/time_reset', service_class=SetBool, handler=time_reset)

    # keep node alive
    rospy.spin()