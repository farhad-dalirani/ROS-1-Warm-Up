#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int64

def callback_for_number_topic(msg):
    rospy.loginfo('Number Topic message is: {}'.format(msg.data))


def callback_for_string_topic(msg):
    rospy.loginfo('String Topic message is: {}'.format(msg.data))

if __name__ == '__main__':
    
    # initiate rosnode
    rospy.init_node(name='subscriber_to_number_and_string_topic')

    # subscribe to the number topic
    sub_num = rospy.Subscriber(name='/number_topic', data_class=Int64, callback=callback_for_number_topic)


    # subscribe to the string topic
    sub_num = rospy.Subscriber(name='/string_topic', data_class=String, callback=callback_for_string_topic)


    # keep node and its thread alive
    rospy.spin()
    