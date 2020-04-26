# ECE470_project

This project is for UIUC ECE 470 SP 2020. The readme inside the file is how to set up the copellia sim python API. The probram has 2 operating modes, forward and inverse kinematics. Either can be chosen by typing F for forward and I for inverse when prompted.

Forward Kinematics:

The forward kinematics code will prompt you for 6 space seperated degrees joint angles for the robot to move to. The robot will then move to that configuration and print out the final transform and give any warnings or errors in connecting with the simulation.

Inverse Kinematics:

The inverse kinematics code will prompt you for an XYZ location and print out the accosiated joint angles in radians. The S,M, and desired end effector matrix will print for debugging purposes. If you want to change the rotation of the final location you'll have to go into the code and modify the desired end effector matrix.

Final_enviroment and Main.py

This file contains the final coppelia sim enviroment, run main to run the program. 3 waypoint mapped welding paths are preprogramed, a line, a corner shape, and a full square. The user inputs an S for the stick weld torch, M for the Mig weld torch, and T for Tig weld torch, then the next prompt will ask for S for square, L for line, and C for corner, H is to be developed but will display some info on weld types. For proper opperation the port in coppellia sim needs to be opened (simRemoteApi.start(19999) in coppelia terminal)
