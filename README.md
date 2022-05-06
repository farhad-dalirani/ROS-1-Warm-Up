## About this repository, ROS 1 Warm-up:
This repository contains code, instructions, commands, etc for Robotic Operating System (ROS 1) for the purpose of education and Warming-up.


## Install ROS Noetic
install ROS Noetic as it is explained here: [Installation Guide](http://wiki.ros.org/noetic/Installation/Ubuntu).<br />
Other versions can be installed. The instaliation link can be find of official website of ROS.

## Set-up Catkin work space:
```
mkdir catkin_ws
cd catkin_ws/
mkdir src
catkin_make
cd devel/
source setup.bash
```

Add this to the end of .bashrc file:<br />
`source ~/catkin_ws/devel/setup.bash`<br />

## Create a package:<br />
First chage directory: `cd catkin_ws/src/`. Then, create package by using `catkin_create_pkg package-name dependencies name`. For example, `catkin_create_pkg my_first_package roscpp rospy std_msgs`. After that, we should go to `catkin_ws` and make again by using `catkin_make`.<br />

For creating node by Python after making the new package, we can go to the directory of the new package inside catkin workstation and create a folder that is named `scripts`. We can put out python code inside this folder. We create a python file and make it executable by using `chmod +x file-name.py`. Making the catkin workspace after adding Python nodes is not necessary.


## Install already existing ROS packages
We can use this command in terminal to install an existing ROS package:
```
sudo apt-get install ros-noetic-package-name
```

For example, `sudo apt-get install ros-noetic-turtlesim`.

## Add dependencies to an already existing package:
Go to package directory in catkin work space, then, modify `CMakelist.txt` and `package.xml`. 

## Check validity of installation of ROS and Catkin workstation:
Install tutle package:
```
sudo apt-get install ros-noetic-turtlesim
```
Initiate master:
```
roscore
```
Run Turtle similator:
```
rosrun turtlesim turtlesim_node
```
Run key controls for the turtle:
```
rosrun turtlesim turtle_teleop_key
```


## ROS command:
`roscore`: It starts ROS master.<br />
`rosrun package-name node-name`: It executes a node inside a package.<br />
`rosrun rqt_graph rqt_graph`: It plots nodes in ROS's graph. Turn-off debuh checkbox for showing all details.<br />
`rosnode info /node-name`: It prints information related to a node.<br />
`rosnode list`: It prints name of nodes that are being executed.<br />
`rosnode ping /node-name`: It is useful to check ping and connectivity of a node and master.<br />
`rosnode kill /node-name`: It terminates a node.<br />
`rostopic -h`: Shows all commands related to rostopic.<br />
`rostopic list`: List all existing topics on graph.<br />
`rostopic echo /topic-name`: Listen to a topic in terminal. <br />
`rostopic info /topic-name`: Information related to a topic such as message type and punlisher node.<br />
`rostopic pub -r 5 topic-name std_msgs:String "data: 'Hello world!'"`: Publish in a topic from terminal.<br />
`rosservice -h`: Shows all commands related to ros service.<br />
`rosservice list`: List all existing topics on graph.<br />
`rosservice call /sevice-name msg`: request from a service in terminal.<br />
`rosservice args /sevice-name`: print message's arguments of a service.<br />
`rosservice info /sevice-name`: print service information such as node name.<br />


## ROS Python:
Import ros package in Python:
```
import rospy
```

Import message in python:
```
import std_msgs
from std_msgs.msg import String
```

Initial a node:
```
rospy.init_node('node name')
```
Ititial a node with anonymous method to be able to run several instance simultanously:
```
rospy.init_node('node name', anonymous=True)
```

Log information:
```
rospy.loginfo('message')
rospy.logwarn('message')
```

Rate object for spleep, etc:
```
rate = rospy.Rate(10)
rate.sleep()
```

Check shoutdown flag has been sent or not:
```
rospy.is_shutdown()
```

Create publisher:
```
pub = rospy.Publisher(name='/name', data_class=String (or other type), queue_size)
```

Publish message:
```
publisher_obj.publish(msg)
```

Create string message:
```
msg = String()
msg.data = "Hi, this is me from the Robot news Radio!"
```

Create a subscriber:
```
sub = rospy.Subscriber(name='/topic-name', data_class, callback)
```

Keep a node and all its threads untill shoutdown flag:
```
rospy.spin()
```

Create a service:
```
rospy.Service('/server-name', message-to-server-type, request-handler-function)
```

Wait for a service to be started:
```
rospy.wait_for_service('/service-name')
```

Create the client:
```
client_obj = rospy.ServiceProxy('/service-name', message_type)
```

Call the service:
```
result = client_obj(message arguments)
```

