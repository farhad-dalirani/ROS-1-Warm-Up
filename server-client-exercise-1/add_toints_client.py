#!/usr/bin/env python3



import rospy
from rospy_tutorials.srv import AddTwoInts

if __name__ == '__main__':
    
    # node name
    rospy.init_node('add_two_ints_client')

    # wait for the service to be started
    rospy.wait_for_service('/add_two_ints')


    try:
        # create the client
        add_two_ints = rospy.ServiceProxy('/add_two_ints', AddTwoInts)

        # call service
        response = add_two_ints(2, 4)

        rospy.loginfo('Sum is: {}'.format(response.sum))
    except rospy.ServiceException as e:
        rospy.logwarn('Service Failed" {}'.format(e))
