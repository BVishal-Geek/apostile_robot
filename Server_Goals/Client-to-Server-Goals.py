#!/usr/bin/env python

import rospy 
import actionlib 
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal #move base action deals with the server, to check whether it is turned on
def movebase_client():
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()

    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 1.9298482789265212
    goal.target_pose.pose.position.y = -3.4477901668376445
    
    goal.target_pose.pose.orientation.w = 0.7676128778237906

    

    
    client.send_goal(goal)
    wait = client.wait_for_result()

    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result() 
    if __name__ == '__main__':
        try:
            rospy.init_node('movebase_client')
            result = movebase_client()
            if result:
                rospy.loginfo("Goal execution Done")
        except ROSInterruptException:
            rospy.loginfo("execution Done")

    

