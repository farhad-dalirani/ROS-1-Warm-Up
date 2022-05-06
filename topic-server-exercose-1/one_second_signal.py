#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64


if __name__ == '__main__':

    # initial node
    rospy.init_node('one_second_signal')

    # rate for sleep
    rate = rospy.Rate(1)

    # create topic
    pub = rospy.Publisher(name='/one_second_signal', data_class=Int64, queue_size=10)

    # while the shout down signal has not recieved
    while not rospy.is_shutdown():
        
        # publish on topic
        pub.publish(1)

        # wait one second
        rate.sleep()

    rospy.loginfo('one_second_signal node was closed.')