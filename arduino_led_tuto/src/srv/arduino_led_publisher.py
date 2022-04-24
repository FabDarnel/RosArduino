#!/usr/bin/env python 
import pyfirmata
import time
import rospy    # import rospy to write the ROS node
from std_msgs.msg import String # use the std_msgs/String message type as a simple string container for publishing
# source: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

def talker(): # function talker 
    pub = rospy.Publisher('chatter', String, queue_size = 10)   # declares that the node is publishing to the chatter topic using the String.String message type which is actually the class std_msgs
    rospy.init_node('talker', anonymous=True)   # initialise the node "talker", anonymous = True ensures that the node has a unique name
    rate = rospy.Rate(10)   # 10Hz  creates a Rate object rate to loop at a desired rate
    while not rospy.is_shutdown():
        LED = board.digital[13].write(1)
        pub.publish("1")
        time.sleep(1)
        LED = board.digital[13].write(0)
        pub.publish("0")
        time.sleep(2)

if __name__ == '__main__':
    board = pyfirmata.Arduino('/dev/ttyACM0')
    print("communication with board successful")
    try:
        talker()
    except rospy.ROSInterruptException:
        pass