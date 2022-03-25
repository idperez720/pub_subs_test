#!/usr/bin/env python3
import rospy
from std_msgs import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Recibido: %", data.data)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()