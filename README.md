# RosArduino
Connect and communicate with Arduino Uno using python and ROS Melodic 
The objective of this tutorial is to: 
1.  Connect Aduino Uno to Ubuntu and control its LED (pin 13) using python
2.  Communicate with Arduino Uno digital pin 13 using ROS 

## Table of Contents
1. [General Info](#general-info)
2. [Installation](#installation)
3. [ROS Package](#ros-package)
4. [Run Scrip](#run-script)

## General Info
1. The Robot Operating System (ROS) is a set of software libraries and tools that help you build robot applications. From drivers to state-of-the-art algorithms, and with powerful developer tools, ROS has what you need for your next robotics project. And it's all open source. (https://www.ros.org/)
2. Open-source electronic prototyping platform enabling users to create interactive electronic objects.(https://www.arduino.cc/)
This tutorial aims at being a basic introduction to robotics, interfacing ROS and Arduino Uno. 

## Installation 
1. Install ROS Melodic on Ubuntu 18.04: http://wiki.ros.org/melodic/Installation/Ubuntu
2. Install catkin_tools packages: https://catkin-tools.readthedocs.io/en/latest/installing.html
3. Install Arduino IDE on Ubuntu 18.04: https://docs.arduino.cc/software/ide-v1/tutorials/Linux
4. If you experience " Error opening serial port" refer to: Please Read section at https://docs.arduino.cc/software/ide-v1/tutorials/Linux#toc6
5. Install rosserial: https://maker.pro/arduino/tutorial/how-to-use-arduino-with-robot-operating-system-ros
6. If you have trouble installing rosserial refer to: https://www.youtube.com/watch?v=Y6oo_2qHJII&ab_channel=MieRobot 
7. Create a catkin_ws to save the packages: https://industrial-training-master.readthedocs.io/en/melodic/_source/session1/Create-Catkin-Workspace.html
8. An interesting link to interface Arduino to ROS: https://www.servomagazine.com/magazine/article/november2016_ros-arduino-interfacing-for-robotics-projects

## ROS Package
1. Using the steps provided at [Installation](#installation), create a catki workspace (cakin_ws)
2. Navigate to the catkin_ws: cd ~/catkin_ws/src
3. Use the command catkin_create_pkg script to create new package with dependencies std_msgs roscpp rospy: catkin_create_pkg new_package_name std_msgs rospy roscpp
4. e.g: ![image](https://user-images.githubusercontent.com/104302312/164974119-9a9b3d14-864b-4557-8054-1554de4dcdbf.png)
5. Navigate to the package folder using cd command in the terminal
6. e.g: ![image](https://user-images.githubusercontent.com/104302312/164974159-a33b9abb-a934-4037-95e6-8b543ba2415a.png)
7. Create a service directory in src: 
8. e.g: ![image](https://user-images.githubusercontent.com/104302312/164974183-6c14d061-6e58-42ce-bcd7-4784efd15499.png)

## Run Script
1. After writing the script, use command chmod +x python script to make the script executable
2. e.g: ![image](https://user-images.githubusercontent.com/104302312/164974458-4f3d59c1-10f2-4a31-8e41-d7e206fd88f1.png)
3. ![image](https://user-images.githubusercontent.com/104302312/164974477-7e9fcdd5-d4b4-4966-b382-3d83cbb5c34e.png)
4. Open a new terminal window and run roscore ![image](https://user-images.githubusercontent.com/104302312/164974518-ed55a9e0-d5b1-4d8d-af48-8f867b6be8ad.png)
5. Open a new window and using python command run script ![image](https://user-images.githubusercontent.com/104302312/164974544-578aee17-928c-4adf-8583-bdcbd2e43d50.png)
6. Open a new window and use command line rostopic list to view the topic being broadcasted
7. Use rostopic echo to view the message broadcasted by the publisher
![image](https://user-images.githubusercontent.com/104302312/164974675-d7de96f4-f3df-407b-96f7-a062a3c1e2fd.png)





