#!/usr/bin/env python3

import rospy 
from std_msgs.msg import String

if __name__ == '__main__':

    # initiate node
    rospy.init_node(name='string_generator_node')

    # rate for output, 2 messages per second
    rate = rospy.Rate(2)

    # publisher
    pub = rospy.Publisher(name='/string_topic', data_class=String, queue_size=10)

    number = 0

    # publish until the node recieve shoutdown signal
    while not rospy.is_shutdown():

        # create message
        msg = String()
        msg.data = 'Number is {}'.format(number)

        # publish the message
        pub.publish(msg)

        # increase the number
        number = (number + 1) % 120

        # sleep
        rate.sleep()

    print('String publisher is closed.')