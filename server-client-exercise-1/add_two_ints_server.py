#!/usr/bin/env python3

import rospy
from rospy_tutorials.srv import AddTwoInts

def handle_add_two_ints(req):
    """
    Request handler of the server
    """
    result = req.a + req.b
    rospy.loginfo(
        'Sum of ' + str(req.a) + ' and ' + str(req.b)+ 'is ' +str(result))
    return result

if __name__ == '__main__':

    # node name
    rospy.init_node('add_two_ints_server')
    rospy.loginfo('Add two server node created.')

    service = rospy.Service('/add_two_ints', AddTwoInts, handle_add_two_ints)

    rospy.loginfo('Service has been started.')

    # keep node and all its threads alive until shout down command
    rospy.spin()
    