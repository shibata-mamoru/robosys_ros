#!/usr/bin/env python
# encoding: utf-8
###########################
# Author: Mamoru Shibata
#
###########################

import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    # code
    rospy.init_node('count')
    pub = rospy.Publisher('countprimenum', Int32, queue_size=1)
    rate = rospy.Rate(1)
    num = 1000
    for i in range(2, num):
        for j in range(2, i+1):
            if i % j == 0:
                if i == j:
                    pub.publish(i)
                    rate.sleep()
                else:
                    break

