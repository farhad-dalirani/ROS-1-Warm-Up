![ROS CODE CHEAT SHEET](ROS.png?raw=true)

# Table of contents

- [About this repository, ROS 1 Warm-up tutorial:](#about-this-repository-ros-1-warm-up-tutorial)
- [Resources:](#resources)
- [Install ROS Noetic](#install-ros-noetic)
- [Set-up Catkin work space:](#set-up-catkin-work-space)
- [Create a package:<br />](#create-a-packagebr-)
- [Install existing ROS packages](#install-existing-ros-packages)
- [Add dependencies to an already existing package:](#add-dependencies-to-an-already-existing-package)
- [Check validity of installation of ROS and Catkin workstation:](#check-validity-of-installation-of-ros-and-catkin-workstation)
- [ROS command:](#ros-command)
- [ROS Python:](#ros-python)
- [Useful existing message and sevice packages:](#useful-existing-message-and-sevice-packages)
- [Create a new message type:](#create-a-new-message-type)
- [Create a new service type:](#create-a-new-service-type)
- [Create Launch file:](#create-launch-file)

# About this repository, ROS 1 Warm-up tutorial:
This repository contains code, instructions, commands, etc for Robotic Operating System (ROS 1) for the purpose of education and Warming-up.

# Resources:
- ROS Wiki
- ROS Answers
- ROS Discourse

# Install ROS Noetic
install ROS Noetic as it is explained here: [Installation Guide](http://wiki.ros.org/noetic/Installation/Ubuntu).<br />
Other versions can be installed. The instaliation link can be find of official website of ROS.

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
```
source ~/catkin_ws/devel/setup.bash
```

We can create as many catkin workstations as we want by following the above method. However, we should go to .bashrc file and comment all of them except the one that we want to use.

# Create a package:<br />
First chage directory: `cd catkin_ws/src/`. Then, create package by using `catkin_create_pkg package-name dependencies name`. For example, `catkin_create_pkg my_first_package roscpp rospy std_msgs`. After that, we should go to `catkin_ws` and make again by using `catkin_make`.<br />

For creating node by Python after making the new package, we can go to the directory of the new package inside catkin workstation and create a folder that is named `scripts`. We can put out python code inside this folder. We create a python file and make it executable by using `chmod +x file-name.py`. Making the catkin workspace after adding Python nodes is not necessary.


# Install existing ROS packages
We can use this command in terminal to install an existing ROS package:
```
sudo apt-get install ros-noetic-package-name
```

For example, `sudo apt-get install ros-noetic-turtlesim`.

# Add dependencies to an already existing package:
Go to package directory in catkin work space, then, modify `CMakelist.txt` and `package.xml`.

# Check validity of installation of ROS and Catkin workstation:
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


# ROS command:
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
`rosservice info /sevice-name`: print service information such as node name.<br />
`rosservice list`: List all existing topics on graph.<br />
`rosservice call /sevice-name msg`: request from a service in terminal.<br />
`rosservice args /sevice-name`: print message's arguments of a service.<br /> 
`rosmsg -h`: Shows description for different command for message files.<br />
`rossrv -h`: Shows description for different command for message files.<br />
`rosmsg show message_file_name`: Shows fields of a message type.<br />
`rossrv show service_file_name`: Shows fields of a service type.<br />
`rosmsg list | grep message_package_name`: See our created message data type. It should be enter in catkin workstation<br />
`rosparam -h`: Show commands related to ROS parameter. <br />
`rosparam list`: List of all existing parameters. <br />
`rosparam set /programmer "Farhad"`: Set a new paramerosparam get /sensor_read_frequency 
ters. <br />
`rosparam get /sensor_read_frequency `: Get value of a parameter. <br />
`rosbag -h`: It shows commands related to ROS bag.
`rosbag record /name-of-topic`: Record a topic. It creates `.bag` file.
`rosbag info name-of-bag-file.bag`: It shows information related to a bag file such as path, duration, start and end time, number of messages, message type, topic name, etc.
`rosbag play name-of-bag-file.bag`: It plays messages inside the `.bag` file as it was generated. We can create a subscriber to the topic and use the recorded messages.

# ROS Python:
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

Get a ros parameter in Python code:
```
publish_frequency = rospy.get_param('/number_publish_frequency')
```

# Useful existing message and sevice packages:
```
std_msgs
sensor_msgs
geometry_msgs
std_srvs
```

# Create a new message type:
For avoiding dependency issues and usability, it is good idea to create a new messsage type inside a dedicated message package. For example:
```
cd catkin_ws/src
catkin_create_pkg my_robot_msgs roscpp rospy std_msgs
cd my_robot_msgs
rm -rf include/
rm -rf src/
```
Then we should edit `package.xml` by adding these two lines:
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```
Then we should edit `CMakeLists.txt file`. First, we add `message_generation` to `find_package` section. For example:
```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)
```
Second, we should uncomment this commented section:
```
## Generate added messages and services with any dependencies listed here
# generate_messages(
#   DEPENDENCIES
#   std_msgs
# )
```
as below:
```
generate_messages(
  DEPENDENCIES
  std_msgs
)
```

Third, we uncomment and add the below section:
```
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES my_robot_msgs
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)
```
as following:
```
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES my_robot_msgs
   CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
#  DEPENDS system_lib
)
```
After editing `CMakeLists.txt` we create a folder besides `CMakeLists` and `package.xml`:
```
mkdir msg
cd msg
```
It must be msg. Then we can create message code file. For example:
```
touch HardwareStatus.msg
```
This is an example of a new message type which we put in `HardwareStatus.msg`:
```
int64 temperature
bool are_motors_up
string debug_message
```
All of them are standard msg types that are provided by ROS.

Again, we should edit `CMakeLists.txt` again by editing following section:
```
## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

```
as below:
```
## Generate messages in the 'msg' folder
add_message_files(
  FILES
  HardwareStatus.msg
)

```
Finally, we should back to `catkin_ws` folder and make the new package by `catkin_make`. Now the new package that contain the new message type can be added as a dependency into a package. Therefore, we will be able to use the new message type.<br />
To add message package to another package, we should first go to the target package folder. For example, we go to `my_ros_turorials`:
```
cd src/my_robot_rurorials/
```
After that first, we should edit `package.xml` by adding this line:
```
<depend>my_robot_msgs</depend>
```
Second, we should edit `CMakeList.txt` by changing:
```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  std_srvs
)
```
As below:
```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  std_srvs
  my_robot_msgs
)
```
 After these step terminals should be reopend and in case of problem, in catkin workspace these commands should be entered:
 ```
 source ~/.bashrc
 ```
 yet if it did not work:
 ```
 source catkin_ws/devel/setup.bash
 ```

# Create a new service type:
It is similar to `Create a new message type` section. First, we go to the package that dedicated to the new message and service type, in our example it is `my_robot_message` package. Then, we create a folder with the name of `srv`. After that we create the new sevice file:
```
mkdir srv
cd srv
touch ComputeDiskArea.srv
```
For example, we create this service type:
```
float64 radius
---
float64 area
```
The 3 dashes are necessary. It separates service request and service response.

Using the new service type in another package is like using a new message type in `Create a new message type` section.

# Create Launch file:
It is better to put launch files in a separate ROS package; however, they can be put in any package. First, we go to Catkin workstation, `src` folder. After that we create a new package:

```
cd catkin_ws/src/
catkin_create_pkg my_robot_bringup
```
Then, we should back to catkin workstation and make the catkin workstation:
```
catkin_make
```
After that, we go to package folder and create a folder with the name of `launch`:
```
cd src/my_robot_bringup/
mkdir launch
```
Then inside the launch folder, we create our launch file with the extension of `.launch`:
```
touch number_app.launch
```
Is `chmod +x file-name` required?
Now, inside the launch file, we can determine parameters and nodes that are needed to created after calling the launch file:
```
<launch>

    <param name="/number_publish_frequency" type="double" value="3.0" />
    <param name="/number_to_publish" type="int" value="10" />

    <node name="number_generator" pkg="my_robot_rurorials" type="number_generator.py" />

</launch>
```
`node name=""` overwrites the node name that specified in the node file. We can select identical node name or a different name. 

In this way we can call a ros launch file, it it does not work, we should go to the directory of launch file:
```
roslaunch my_robot_bringup number_app.launch
```
this command checks for `roscore`, if it is not running, it execute `roscore` before launching.

<br />
<br />

---

# Famous ROS packages:
This part has instructions for some of the most famous ROS packages that I use for my PhD thesis.

## ROS Wrapper for Intel RealSense Device:
It can be installed according to this tutorial:
```
https://github.com/IntelRealSense/realsense-ros
```

The default execution of the Intel RealSense Device is as follow:
```
roslaunch realsense2_camera rs_camera.launch
```

## ROS RVIZ:
The ROS package is used to visualised different kind of information such as images, point clouds, etc.
```
http://wiki.ros.org/rviz/UserGuide
```
One one the ways to execute RVIZ is:
```
rosrun rviz rviz
```

At the `Displays` section of RVIZ's GUI, there is an `Add` button. After clicking on it, we can visualize a topic with two ways:
1- By display type tab in the opened window
2- By topic type tab in the opened window
The second one is easier.

## ROS Basler Pylon ROS Camera
It can be isntalled according to:
```
https://github.com/basler/pylon-ros-camera
```

