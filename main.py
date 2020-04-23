import numpy as np
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

torch_type = input('Input:welder type S(stick),M(mig),T(tig)')
if(torch_type=='S' or torch_type == 's'):
    print("Stick welding chosen")
if(torch_type=='M' or torch_type == 'm'):
    print("Mig welding chosen")
if(torch_type=='T' or torch_type == 't'):
    print("Tig welding chosen")
else:
    print("unrecognised welding type")

Weld_path = input('Input: Chose weld path (1, 2, or 3) if unsure enter H')
if(torch_type=='1'):
    print("Welding path 1 chosen")
if(torch_type=='2'):
    print("Welding path 2 chosen")
if(torch_type=='3'):
    print("Welding path 3 chosen")
if(torch_type=='H' or torch_type == 'h'):
    print("Print data on weld paths")
else:
    print("unrecognised welding path")


theta = [0,0,0,0,np.pi/2,np.pi/2]
velocities = [1,1,1,1,1,1]
error_code, POI = sim.simxGetObjectHandle(clientID,'POI',sim.simx_opmode_blocking)
error_code, conveyor   = sim.simxGetObjectHandle(clientID,'customizableConveyor',sim.simx_opmode_blocking)
error_code, rangefinder = sim.simxGetObjectHandle(clientID,'fastHokuyo',sim.simx_opmode_blocking)
error_code, scanner = sim.simxGetObjectHandle(clientID,'LaserScanner_2D',sim.simx_opmode_blocking)
error_code, stick = sim.simxGetObjectHandle(clientID,'StickTorch',sim.simx_opmode_blocking)
error_code, mig   = sim.simxGetObjectHandle(clientID,'MigTorch',sim.simx_opmode_blocking)
error_code, tig   = sim.simxGetObjectHandle(clientID,'TigTorch',sim.simx_opmode_blocking)


error_code, UR3_joint1 = sim.simxGetObjectHandle(clientID,'UR3_joint1',sim.simx_opmode_blocking)
error_code, UR3_joint2 = sim.simxGetObjectHandle(clientID,'UR3_joint2',sim.simx_opmode_blocking)
error_code, UR3_joint3 = sim.simxGetObjectHandle(clientID,'UR3_joint3',sim.simx_opmode_blocking)
error_code, UR3_joint4 = sim.simxGetObjectHandle(clientID,'UR3_joint4',sim.simx_opmode_blocking)
error_code, UR3_joint5 = sim.simxGetObjectHandle(clientID,'UR3_joint5',sim.simx_opmode_blocking)
error_code, UR3_joint6 = sim.simxGetObjectHandle(clientID,'UR3_joint6',sim.simx_opmode_blocking)
error_code, UR3_joint6 = sim.simxGetObjectHandle(clientID,'UR3_joint6',sim.simx_opmode_blocking)


return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint1,velocities[0],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint2,velocities[1],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint3,velocities[2],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint4,velocities[3],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint5,velocities[4],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint6,velocities[5],sim.simx_opmode_blocking)

return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,theta[0],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,theta[1],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,theta[2],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,theta[3],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,theta[4],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,theta[5],sim.simx_opmode_blocking)



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
