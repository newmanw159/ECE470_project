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

FvI = input('F for forward Kinematics, I for Inverse Kinematics')
if(FvI=='F' or FvI == 'f'):
    print("input 6 space seperated angles in degrees")
    theta = [float(i)*numpy.pi/180 for i in input().split()]
    #print(theta)
    location = project_helper_func.forward_ur3_kin(theta)
    print('location \n',location)
    XYZ = [location.item(3),location.item(7),location.item(11)]
    #sim.simxAddStatusbarMessage(clientID,'XYZ Pos',sim.simx_opmode_oneshot)
    #sim.simxAddStatusbarMessage(clientID,location,sim.simx_opmode_oneshot)
if(FvI=='I' or FvI == 'i'):
    theta_corrected = []
    print("input 3 space seperated X Y Z values in Meters")
    target = [float(i) for i in input().split()]
    final_endeffector= numpy.array([[ 0.77309907, -0.5458005,   0.32314029, -0.20719392],\
                                    [ 0.62340519,  0.55988193, -0.5458005,  -0.21503198],\
                                    [ 0.11697778,  0.62340519,  0.77309907,  0.62887313],\
                                    [ 0.0        ,  0.0        ,  0.0        ,  1.0]])
    thetas = numpy.array([20, -20, 20, -20, 20, -20])
    theta = project_helper_func.inverseKin(final_endeffector,thetas)

velocities = [1,1,1,1,1,1]
error_code, POI = sim.simxGetObjectHandle(clientID,'POI',sim.simx_opmode_blocking)
#print ('errorcodePOI =',error_code)
error_code, UR3_joint1 = sim.simxGetObjectHandle(clientID,'UR3_joint1',sim.simx_opmode_blocking)
#print ('errorcode1 =',error_code)
error_code, UR3_joint2 = sim.simxGetObjectHandle(clientID,'UR3_joint2',sim.simx_opmode_blocking)
#print ('errorcode2 =',error_code)
error_code, UR3_joint3 = sim.simxGetObjectHandle(clientID,'UR3_joint3',sim.simx_opmode_blocking)
#print ('errorcode3 =',error_code)
error_code, UR3_joint4 = sim.simxGetObjectHandle(clientID,'UR3_joint4',sim.simx_opmode_blocking)
#print ('errorcode4 =',error_code)
error_code, UR3_joint5 = sim.simxGetObjectHandle(clientID,'UR3_joint5',sim.simx_opmode_blocking)
#print ('errorcode5 =',error_code)
error_code, UR3_joint6 = sim.simxGetObjectHandle(clientID,'UR3_joint6',sim.simx_opmode_blocking)
#print ('errorcode6 =',error_code)
#error_code, Gripper = sim.simxGetObjectHandle(clientID,'Gripper',sim.simx_opmode_blocking)

#sim.simxStartSimulation(clientID,sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint1,velocities[0],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint2,velocities[1],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint3,velocities[2],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint4,velocities[3],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint5,velocities[4],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint6,velocities[5],sim.simx_opmode_blocking)

#sim.simxPauseCommunication(clientID,True)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,theta[0],sim.simx_opmode_blocking)
#print('returncode1=',return_code)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,theta[1],sim.simx_opmode_blocking)
#print('returncode2=',return_code)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,theta[2],sim.simx_opmode_blocking)
#print('returncode3=',return_code)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,theta[3],sim.simx_opmode_blocking)
#print('returncode4=',return_code)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,theta[4],sim.simx_opmode_blocking)
#print('returncode5=',return_code)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,theta[5],sim.simx_opmode_blocking)
#print('returncode6=',return_code)
#sim.simxPauseCommunication(clientID,False)
if(FvI=='F' or FvI == 'f'):
    sim.simxSetObjectPosition(clientID,POI,-1,XYZ,sim.simx_opmode_blocking)

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
