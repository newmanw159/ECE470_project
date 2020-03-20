import numpy
import sim
import time
import sys
import math
import project_helper_func


print('program start')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID==-1:
    print ('Not connected to remote API server')
    sys.exit()
else:
    print('Connected to remote API server')

theta = [math.pi/4,-1*math.pi/4,math.pi/4,-1*math.pi/4,math.pi/4,-1*math.pi/4]

#theta = [0,0,0,0,0,math.pi/2]

velocities = [1,1,1,1,1,1]
error_code, POI = sim.simxGetObjectHandle(clientID,'POI',sim.simx_opmode_blocking)
error_code, UR3_joint1 = sim.simxGetObjectHandle(clientID,'UR3_joint1',sim.simx_opmode_blocking)
error_code, UR3_joint2 = sim.simxGetObjectHandle(clientID,'UR3_joint2',sim.simx_opmode_blocking)
error_code, UR3_joint3 = sim.simxGetObjectHandle(clientID,'UR3_joint3',sim.simx_opmode_blocking)
error_code, UR3_joint4 = sim.simxGetObjectHandle(clientID,'UR3_joint4',sim.simx_opmode_blocking)
error_code, UR3_joint5 = sim.simxGetObjectHandle(clientID,'UR3_joint5',sim.simx_opmode_blocking)
error_code, UR3_joint6 = sim.simxGetObjectHandle(clientID,'UR3_joint6',sim.simx_opmode_blocking)
#error_code, Gripper = sim.simxGetObjectHandle(clientID,'Gripper',sim.simx_opmode_blocking)
print ('errors = ',error_code)
#sim.simxStartSimulation(clientID,sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint1,velocities[0],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint2,velocities[1],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint3,velocities[2],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint4,velocities[3],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint5,velocities[4],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint6,velocities[5],sim.simx_opmode_blocking)

#sim.simxPauseCommunication(clientID,True)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,theta[0],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,theta[1],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,theta[2],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,theta[3],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,theta[4],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,theta[5],sim.simx_opmode_blocking)
#sim.simxPauseCommunication(clientID,False)

location = project_helper_func.forward_ur3_kin(theta)
print('location \n',location)
XYZ = [location.item(3),location.item(7),location.item(11)]
sim.simxSetObjectPosition(clientID,POI,-1,XYZ,sim.simx_opmode_blocking)


#sim.simxAddStatusbarMessage(clientID,'XYZ Pos',sim.simx_opmode_oneshot)
#sim.simxAddStatusbarMessage(clientID,location,sim.simx_opmode_oneshot)
sim.simxAddStatusbarMessage(clientID,'End of Code',sim.simx_opmode_oneshot)
print('End of Code')
res = input('reset? y/n:')
#print(res)
if(res == 'y'or res ==1):
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetObjectPosition(clientID,POI,-1,[-0.2700,0.01,0.652],sim.simx_opmode_blocking)
