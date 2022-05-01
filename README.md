# About this repository:
This repository contains code, instructions, commands, etc for Robotic Operating System for Warming-up (ROS 1).


# Install ROS Noetic
install ROS Noetic as it is explained here: [Installation Guide](http://wiki.ros.org/noetic/Installation/Ubuntu)

# Set-up Catkin work space:
```
mkdir catkin_ws
cd catkin_ws/
mkdir src
catkin_make
cd devel/
source setup.bash
```

Add this to the end of .bashrc file:
`source ~/catkin_ws/devel/setup.bash`

create a package:
First chage directory: `cd catkin_ws/src/`. Then, create package by using `catkin_create_pkg package-name dependencies name`. For example, `catkin_create_pkg my_first_package roscpp rospy std_msgs`. After that, we should go to `catkin_ws` and make again by using `catkin_make`.

For creating node by Python after making the new package, we can go to the directory of the new package inside catkin workstation and create a folder that is named `scripts`. We can put out python code inside this folder. We create a python file and make it executable by using `chmod ~x file-name.py`. Making the catkin workspace after adding Python nodes is not necessary.


# ROS command:
`roscore`: It starts ROS master.
`rosrun package-name node-name`: It executes a node inside a package.
`rosrun rqt_graph rqt_graph`: It plots nodes in ROS's graph. Turn-off debuh checkbox for showing all details.
`rosnode info /node-name`: It prints information related to a node.
`rosnode list`: It prints name of nodes that are being executed.
`rosnode ping /node-name`: It is useful to check ping and connectivity of a node and master.
`rosnode kill /node-name`: It terminates a node. 



# ROS python:
