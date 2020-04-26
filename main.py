import numpy as np
import sim
import time
import sys
import math
import project_helper_func


processed_parts = 0
num_parts = 2 
countdown = 100000
Weld_start = np.radians([0,0,45,10,-90,0])
zero_loc = np.zeros(6)
print('program start')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID==-1:
    print ('Not connected to remote API server')
    sys.exit()
else:
    print('Connected to remote API server')


theta = [0,0,0,0,0,0]
velocities = [1,1,1,1,1,1]
error_code, POI = sim.simxGetObjectHandle(clientID,'POI',sim.simx_opmode_blocking)
error_code, conveyor   = sim.simxGetObjectHandle(clientID,'ConveyorBelt',sim.simx_opmode_blocking)
error_code, rangefinder = sim.simxGetObjectHandle(clientID,'fastHokuyo',sim.simx_opmode_blocking)
error_code, scanner = sim.simxGetObjectHandle(clientID,'LaserScanner_2D',sim.simx_opmode_blocking)
error_code, stick = sim.simxGetObjectHandle(clientID,'StickTorch',sim.simx_opmode_blocking)
error_code, mig   = sim.simxGetObjectHandle(clientID,'MigTorch',sim.simx_opmode_blocking)
error_code, tig   = sim.simxGetObjectHandle(clientID,'TigTorch',sim.simx_opmode_blocking)
error_code, grip   = sim.simxGetObjectHandle(clientID,'BaxterGripper',sim.simx_opmode_blocking)

return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_close',0,sim.simx_opmode_blocking)
return_code = sim.simxSetIntegerSignal(clientID,'Weld_start',0,sim.simx_opmode_blocking)
return_code = sim.simxSetIntegerSignal(clientID,'released',0,sim.simx_opmode_blocking)

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

return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,0,sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,0,sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,0,sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,0,sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,0,sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,0,sim.simx_opmode_blocking)


torch_type = input('Input:welder type S(stick),M(mig),T(tig)')
if(torch_type=='S' or torch_type == 's'):
    print("Stick welding chosen")
    #theta_stick = np.radians([90,0,0,0,0,0])
    theta = np.radians([90,0,0,0,0,0])
    grab = [1,0,0]
    
elif(torch_type=='M' or torch_type == 'm'):
    print("Mig welding chosen")
    #theta_mig = np.radians([90,45,-90,0,0,0])
    theta = np.radians([90,45,-90,0,0,0])
    grab = [0,1,0]
elif(torch_type=='T' or torch_type == 't'):
    print("Tig welding chosen")
    #theta_tig = np.radians([90,60,-120,0,0,0])
    theta = np.radians([90,60,-120,0,0,0])
    grab = [0,0,1]
else:
    print("unrecognised welding type")

Weld_path = input('Input: Chose weld path (S)quare, (L)ine, (C)orner if unsure enter H')
if(Weld_path== 'S' or Weld_path == 's'):
    print("Square welding path chosen")
    path = 'square'
elif(Weld_path=='L' or Weld_path == 'l'):
    print("Line welding path chosen")
    path = 'line'
elif(Weld_path=='C' or Weld_path == 'c'):
    print("Corner welding path chosen")
    path = "corner"
elif(Weld_path=='H' or Weld_path == 'h'):
    print("Print data on weld paths")
else:
    print("unrecognised welding path")

return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,theta[0],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,theta[1],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,theta[2],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,theta[3],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,theta[4],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,theta[5],sim.simx_opmode_blocking)
time.sleep(10)
return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_stick',grab[0],sim.simx_opmode_blocking)
return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_mig',grab[1],sim.simx_opmode_blocking)
return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_tig',grab[2],sim.simx_opmode_blocking)

#print(sim.simxGetIntegerSignal(clientID,'BaxterGripper_close',sim.simx_opmode_blocking))
return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_close',1,sim.simx_opmode_blocking)
time.sleep(5)
#print(return_code)
#print(sim.simxGetIntegerSignal(clientID,'BaxterGripper_close',sim.simx_opmode_blocking))

return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,zero_loc[0],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,zero_loc[1],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,zero_loc[2],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,zero_loc[3],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,zero_loc[4],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,zero_loc[5],sim.simx_opmode_blocking)

return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,Weld_start[0],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,Weld_start[1],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,Weld_start[2],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,Weld_start[3],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,Weld_start[4],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,Weld_start[5],sim.simx_opmode_blocking)
#return_code = sim.simxSetIntegerSignal(clientID,'_close',1,sim.simx_opmode_oneshot)

weld_velocities = [0.01,0.01,0.01,0.01,0.01,0.01]

return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint1,weld_velocities[0],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint2,weld_velocities[1],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint3,weld_velocities[2],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint4,weld_velocities[3],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint5,weld_velocities[4],sim.simx_opmode_blocking)
return_code = sim.simxSetJointTargetVelocity(clientID,UR3_joint6,weld_velocities[5],sim.simx_opmode_blocking)

return_code = sim.simxSetIntegerSignal(clientID,'Weld_start',1,sim.simx_opmode_blocking)
#while(sim.simxGetIntegerSignal(clientID,'newpart',sim.simx_opmode_blocking)!=1):
#    a=1
while(processed_parts<num_parts):
    return_code,signal=sim.simxGetIntegerSignal(clientID,'newpart',sim.simx_opmode_blocking)
    if(signal==1):
        forward_array = project_helper_func.forward_ur3_kin(Weld_start)
        print(forward_array)

        delta1 = np.array([[0,0,0,-0.0043],\
                      [0,0,0,0],\
                      [0,0,0,0],\
                      [0,0,0,0]])
        waypoint1 = forward_array + delta1
        waypoint_ang1 = project_helper_func.inverseKin(waypoint1,Weld_start)
        for i in range(0,len(waypoint_ang1)):
            while abs(waypoint_ang1[i])>np.pi*2:
                waypoint_ang1[i]=(abs(waypoint_ang1[i])-np.pi*2)*waypoint_ang1[i]/abs(waypoint_ang1[i])

        print('waypoint_ang1=',waypoint_ang1)
        print('waypoint1=',waypoint1,'\n')
        print('calc_waypoint1=',project_helper_func.forward_ur3_kin(waypoint_ang1),'\n')

        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang1[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang1[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang1[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang1[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang1[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang1[5],sim.simx_opmode_blocking)
        ##time.sleep(1)
        delta1_1 = np.array([[0,0,0,-0.0086],\
                      [0,0,0,0],\
                      [0,0,0,0],\
                      [0,0,0,0]])
        waypoint1_1 = forward_array + delta1_1
        waypoint_ang1_1 = project_helper_func.inverseKin(waypoint1_1,waypoint_ang1)
        for i in range(0,len(waypoint_ang1_1)):
            while abs(waypoint_ang1_1[i])>np.pi*2:
                waypoint_ang1_1[i]=(abs(waypoint_ang1_1[i])-np.pi*2)*waypoint_ang1_1[i]/abs(waypoint_ang1_1[i])

        print('waypoint_ang1=',waypoint_ang1_1)
        print('waypoint1=',waypoint1_1,'\n')
        print('calc_waypoint1=',project_helper_func.forward_ur3_kin(waypoint_ang1_1),'\n')

        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang1_1[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang1_1[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang1_1[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang1_1[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang1_1[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang1_1[5],sim.simx_opmode_blocking)
        ##time.sleep(1)
        delta1_2 = np.array([[0,0,0,-0.0128],\
                      [0,0,0,0],\
                      [0,0,0,0],\
                      [0,0,0,0]])
        waypoint1_2 = forward_array + delta1_2
        waypoint_ang1_2 = project_helper_func.inverseKin(waypoint1_2,waypoint_ang1_1)
        for i in range(0,len(waypoint_ang1_2)):
            while abs(waypoint_ang1_2[i])>np.pi*2:
                waypoint_ang1_2[i]=(abs(waypoint_ang1_2[i])-np.pi*2)*waypoint_ang1_2[i]/abs(waypoint_ang1_2[i])

        print('waypoint_ang1=',waypoint_ang1_2)
        print('waypoint1=',waypoint1_2,'\n')
        print('calc_waypoint1=',project_helper_func.forward_ur3_kin(waypoint_ang1_2),'\n')

        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang1_2[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang1_2[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang1_2[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang1_2[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang1_2[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang1_2[5],sim.simx_opmode_blocking)
        ##time.sleep(1)
        delta1_3 = np.array([[0,0,0,-0.017],\
                      [0,0,0,0],\
                      [0,0,0,0],\
                      [0,0,0,0]])
        waypoint1_3 = forward_array + delta1_3
        waypoint_ang1_3 = project_helper_func.inverseKin(waypoint1_3,waypoint_ang1_2)
        for i in range(0,len(waypoint_ang1_3)):
            while abs(waypoint_ang1_3[i])>np.pi*2:
                waypoint_ang1_3[i]=(abs(waypoint_ang1_3[i])-np.pi*2)*waypoint_ang1_3[i]/abs(waypoint_ang1_3[i])

        print('waypoint_ang1=',waypoint_ang1_3)
        print('waypoint1=',waypoint1_3,'\n')
        print('calc_waypoint1=',project_helper_func.forward_ur3_kin(waypoint_ang1_3),'\n')

        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang1_3[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang1_3[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang1_3[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang1_3[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang1_3[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang1_3[5],sim.simx_opmode_blocking)
        ##time.sleep(1)
        delta1_4 = np.array([[0,0,0,-0.0214],\
                      [0,0,0,0],\
                      [0,0,0,0],\
                      [0,0,0,0]])
        waypoint1_4 = forward_array + delta1_4
        waypoint_ang1_4 = project_helper_func.inverseKin(waypoint1_4,waypoint_ang1_3)
        for i in range(0,len(waypoint_ang1_4)):
            while abs(waypoint_ang1_4[i])>np.pi*2:
                waypoint_ang1_4[i]=(abs(waypoint_ang1_4[i])-np.pi*2)*waypoint_ang1_4[i]/abs(waypoint_ang1_4[i])

        print('waypoint_ang1=',waypoint_ang1_4)
        print('waypoint1=',waypoint1_4,'\n')
        print('calc_waypoint1=',project_helper_func.forward_ur3_kin(waypoint_ang1_4),'\n')

        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang1_4[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang1_4[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang1_4[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang1_4[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang1_4[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang1_4[5],sim.simx_opmode_blocking)
        ##time.sleep(1)
        delta1_5 = np.array([[0,0,0,-0.0257],\
                      [0,0,0,0],\
                      [0,0,0,0],\
                      [0,0,0,0]])
        waypoint1_5 = forward_array + delta1_5
        waypoint_ang1_5 = project_helper_func.inverseKin(waypoint1_5,waypoint_ang1_4)
        for i in range(0,len(waypoint_ang1_5)):
            while abs(waypoint_ang1_5[i])>np.pi*2:
                waypoint_ang1_5[i]=(abs(waypoint_ang1_5[i])-np.pi*2)*waypoint_ang1_5[i]/abs(waypoint_ang1_5[i])

        print('waypoint_ang1=',waypoint_ang1_5)
        print('waypoint1=',waypoint1_5,'\n')
        print('calc_waypoint1=',project_helper_func.forward_ur3_kin(waypoint_ang1_5),'\n')

        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang1_5[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang1_5[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang1_5[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang1_5[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang1_5[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang1_5[5],sim.simx_opmode_blocking)
        ##time.sleep(1)
        delta1_6 = np.array([[0,0,0,-0.03],\
                      [0,0,0,0],\
                      [0,0,0,0],\
                      [0,0,0,0]])
        waypoint1_6 = forward_array + delta1_6
        waypoint_ang1_6 = project_helper_func.inverseKin(waypoint1_6,waypoint_ang1_5)
        for i in range(0,len(waypoint_ang1_6)):
            while abs(waypoint_ang1_6[i])>np.pi*2:
                waypoint_ang1_6[i]=(abs(waypoint_ang1_6[i])-np.pi*2)*waypoint_ang1_6[i]/abs(waypoint_ang1_6[i])

        print('waypoint_ang1=',waypoint_ang1_6)
        print('waypoint1=',waypoint1_6,'\n')
        print('calc_waypoint1=',project_helper_func.forward_ur3_kin(waypoint_ang1_6),'\n')

        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang1_6[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang1_6[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang1_6[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang1_6[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang1_6[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang1_6[5],sim.simx_opmode_blocking)
        #time.sleep(1)
        if (path == 'corner' or path == 'square'):
            delta2 = np.array([[0,0,0,-0.03],\
                      [0,0,0,0.00285],\
                      [0,0,0,0],\
                      [0,0,0,0]])
            waypoint2 = forward_array + delta2
            waypoint_ang2 = project_helper_func.inverseKin(waypoint2,waypoint_ang1_6)
            for i in range(0,len(waypoint_ang2)):
                while abs(waypoint_ang2[i])>np.pi*2:
                    waypoint_ang2[i]=(abs(waypoint_ang2[i])-np.pi*2)*waypoint_ang2[i]/abs(waypoint_ang2[i])

            print('waypoint_ang2=',waypoint_ang2)
            print('waypoint2=',waypoint2,'\n')
            print('calc_waypoint2=',project_helper_func.forward_ur3_kin(waypoint_ang2),'\n')

            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang2[0],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang2[1],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang2[2],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang2[3],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang2[4],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang2[5],sim.simx_opmode_blocking)
            #time.sleep(1)
            delta2_1 = np.array([[0,0,0,-0.03],\
                      [0,0,0,0.0057],\
                      [0,0,0,0],\
                      [0,0,0,0]])
            waypoint2_1 = forward_array + delta2_1
            waypoint_ang2_1 = project_helper_func.inverseKin(waypoint2_1,waypoint_ang2)
            for i in range(0,len(waypoint_ang2_1)):
                while abs(waypoint_ang2_1[i])>np.pi*2:
                    waypoint_ang2_1[i]=(abs(waypoint_ang2_1[i])-np.pi*2)*waypoint_ang2_1[i]/abs(waypoint_ang2_1[i])

            print('waypoint_ang2=',waypoint_ang2_1)
            print('waypoint2=',waypoint2_1,'\n')
            print('calc_waypoint2=',project_helper_func.forward_ur3_kin(waypoint_ang2_1),'\n')

            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang2_1[0],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang2_1[1],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang2_1[2],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang2_1[3],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang2_1[4],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang2_1[5],sim.simx_opmode_blocking)
            #time.sleep(1)
            delta2_2 = np.array([[0,0,0,-0.03],\
                      [0,0,0,0.00857],\
                      [0,0,0,0],\
                      [0,0,0,0]])
            waypoint2_2 = forward_array + delta2_2
            waypoint_ang2_2 = project_helper_func.inverseKin(waypoint2_2,waypoint_ang2_1)
            for i in range(0,len(waypoint_ang2_2)):
                while abs(waypoint_ang2_2[i])>np.pi*2:
                    waypoint_ang2_2[i]=(abs(waypoint_ang2_2[i])-np.pi*2)*waypoint_ang2_2[i]/abs(waypoint_ang2_2[i])

            print('waypoint_ang2=',waypoint_ang2_2)
            print('waypoint2=',waypoint2_2,'\n')
            print('calc_waypoint2=',project_helper_func.forward_ur3_kin(waypoint_ang2_2),'\n')

            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang2_2[0],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang2_2[1],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang2_2[2],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang2_2[3],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang2_2[4],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang2_2[5],sim.simx_opmode_blocking)
            #time.sleep(1)
            delta2_3 = np.array([[0,0,0,-0.03],\
                      [0,0,0,0.0114],\
                      [0,0,0,0],\
                      [0,0,0,0]])
            waypoint2_3 = forward_array + delta2_3
            waypoint_ang2_3 = project_helper_func.inverseKin(waypoint2_3,waypoint_ang2_2)
            for i in range(0,len(waypoint_ang2_3)):
                while abs(waypoint_ang2_3[i])>np.pi*2:
                    waypoint_ang2_3[i]=(abs(waypoint_ang2_3[i])-np.pi*2)*waypoint_ang2_3[i]/abs(waypoint_ang2_3[i])

            print('waypoint_ang2=',waypoint_ang2_3)
            print('waypoint2=',waypoint2_3,'\n')
            print('calc_waypoint2=',project_helper_func.forward_ur3_kin(waypoint_ang2_3),'\n')

            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang2_3[0],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang2_3[1],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang2_3[2],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang2_3[3],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang2_3[4],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang2_3[5],sim.simx_opmode_blocking)
            #time.sleep(1)
            delta2_4 = np.array([[0,0,0,-0.03],\
                      [0,0,0,0.01428],\
                      [0,0,0,0],\
                      [0,0,0,0]])
            waypoint2_4 = forward_array + delta2_4
            waypoint_ang2_4 = project_helper_func.inverseKin(waypoint2_4,waypoint_ang2_3)
            for i in range(0,len(waypoint_ang2_4)):
                while abs(waypoint_ang2_4[i])>np.pi*2:
                    waypoint_ang2_4[i]=(abs(waypoint_ang2_4[i])-np.pi*2)*waypoint_ang2_4[i]/abs(waypoint_ang2_4[i])

            print('waypoint_ang2=',waypoint_ang2_4)
            print('waypoint2=',waypoint2_4,'\n')
            print('calc_waypoint2=',project_helper_func.forward_ur3_kin(waypoint_ang2_4),'\n')

            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang2_4[0],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang2_4[1],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang2_4[2],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang2_4[3],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang2_4[4],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang2_4[5],sim.simx_opmode_blocking)
            #time.sleep(1)
            delta2_5 = np.array([[0,0,0,-0.03],\
                      [0,0,0,0.01714],\
                      [0,0,0,0],\
                      [0,0,0,0]])
            waypoint2_5 = forward_array + delta2_5
            waypoint_ang2_5 = project_helper_func.inverseKin(waypoint2_5,waypoint_ang2_4)
            for i in range(0,len(waypoint_ang2_5)):
                while abs(waypoint_ang2_5[i])>np.pi*2:
                    waypoint_ang2_5[i]=(abs(waypoint_ang2_5[i])-np.pi*2)*waypoint_ang2_5[i]/abs(waypoint_ang2_5[i])

            print('waypoint_ang2=',waypoint_ang2_5)
            print('waypoint2=',waypoint2_5,'\n')
            print('calc_waypoint2=',project_helper_func.forward_ur3_kin(waypoint_ang2_5),'\n')

            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang2_5[0],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang2_5[1],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang2_5[2],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang2_5[3],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang2_5[4],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang2_5[5],sim.simx_opmode_blocking)
            #time.sleep(1)
            delta2_6 = np.array([[0,0,0,-0.03],\
                      [0,0,0,0.02],\
                      [0,0,0,0],\
                      [0,0,0,0]])
            waypoint2_6 = forward_array + delta2_6
            waypoint_ang2_6 = project_helper_func.inverseKin(waypoint2_6,waypoint_ang2_5)
            for i in range(0,len(waypoint_ang2_6)):
                while abs(waypoint_ang2_6[i])>np.pi*2:
                    waypoint_ang2_6[i]=(abs(waypoint_ang2_6[i])-np.pi*2)*waypoint_ang2_6[i]/abs(waypoint_ang2_6[i])

            print('waypoint_ang2=',waypoint_ang2_6)
            print('waypoint2=',waypoint2_6,'\n')
            print('calc_waypoint2=',project_helper_func.forward_ur3_kin(waypoint_ang2_6),'\n')

            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang2_6[0],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang2_6[1],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang2_6[2],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang2_6[3],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang2_6[4],sim.simx_opmode_blocking)
            return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang2_6[5],sim.simx_opmode_blocking)
            #time.sleep(1)
            
            if path == 'square':
    
                delta3 = np.array([[0,0,0,-0.0257],\
                      [0,0,0,0.02],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint3 = forward_array + delta3
                waypoint_ang3 = project_helper_func.inverseKin(waypoint3,waypoint_ang2_6)
                for i in range(0,len(waypoint_ang3)):
                    while abs(waypoint_ang3[i])>np.pi*2:
                        waypoint_ang3[i]=(abs(waypoint_ang3[i])-np.pi*2)*waypoint_ang3[i]/abs(waypoint_ang3[i])

                print('waypoint_ang3=',waypoint_ang3)
                print('waypoint3=',waypoint3,'\n')
                print('calc_waypoint3=',project_helper_func.forward_ur3_kin(waypoint_ang3),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang3[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang3[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang3[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang3[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang3[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang3[5],sim.simx_opmode_blocking)
                #time.sleep(1)

                delta3_1 = np.array([[0,0,0,-0.0214],\
                      [0,0,0,+0.02],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint3_1 = forward_array + delta3_1
                waypoint_ang3_1 = project_helper_func.inverseKin(waypoint3_1,waypoint_ang3)
                for i in range(0,len(waypoint_ang3_1)):
                    while abs(waypoint_ang3_1[i])>np.pi*2:
                        waypoint_ang3_1[i]=(abs(waypoint_ang3_1[i])-np.pi*2)*waypoint_ang3_1[i]/abs(waypoint_ang3_1[i])

                print('waypoint_ang3=',waypoint_ang3_1)
                print('waypoint3=',waypoint3_1,'\n')
                print('calc_waypoint3=',project_helper_func.forward_ur3_kin(waypoint_ang3_1),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang3_1[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang3_1[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang3_1[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang3_1[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang3_1[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang3_1[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta3_2 = np.array([[0,0,0,-0.017],\
                      [0,0,0,+0.02],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint3_2 = forward_array + delta3_2
                waypoint_ang3_2 = project_helper_func.inverseKin(waypoint3_2,waypoint_ang3_1)
                for i in range(0,len(waypoint_ang3_2)):
                    while abs(waypoint_ang3_2[i])>np.pi*2:
                        waypoint_ang3_2[i]=(abs(waypoint_ang3_2[i])-np.pi*2)*waypoint_ang3_2[i]/abs(waypoint_ang3_2[i])

                print('waypoint_ang3=',waypoint_ang3_2)
                print('waypoint3=',waypoint3_2,'\n')
                print('calc_waypoint3=',project_helper_func.forward_ur3_kin(waypoint_ang3_2),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang3_2[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang3_2[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang3_2[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang3_2[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang3_2[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang3_2[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta3_3 = np.array([[0,0,0,-0.01285],\
                      [0,0,0,+0.02],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint3_3 = forward_array + delta3_3
                waypoint_ang3_3 = project_helper_func.inverseKin(waypoint3_3,waypoint_ang3_2)
                for i in range(0,len(waypoint_ang3_3)):
                    while abs(waypoint_ang3_3[i])>np.pi*2:
                        waypoint_ang3_3[i]=(abs(waypoint_ang3_3[i])-np.pi*2)*waypoint_ang3_3[i]/abs(waypoint_ang3_3[i])

                print('waypoint_ang3=',waypoint_ang3_3)
                print('waypoint3=',waypoint3_3,'\n')
                print('calc_waypoint3=',project_helper_func.forward_ur3_kin(waypoint_ang3_3),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang3_3[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang3_3[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang3_3[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang3_3[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang3_3[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang3_3[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta3_4 = np.array([[0,0,0,-0.00857],\
                      [0,0,0,+0.02],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint3_4 = forward_array + delta3_4
                waypoint_ang3_4 = project_helper_func.inverseKin(waypoint3_4,waypoint_ang3_3)
                for i in range(0,len(waypoint_ang3_4)):
                    while abs(waypoint_ang3_4[i])>np.pi*2:
                        waypoint_ang3_4[i]=(abs(waypoint_ang3_4[i])-np.pi*2)*waypoint_ang3_4[i]/abs(waypoint_ang3_4[i])

                print('waypoint_ang3=',waypoint_ang3_4)
                print('waypoint3=',waypoint3_4,'\n')
                print('calc_waypoint3=',project_helper_func.forward_ur3_kin(waypoint_ang3_4),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang3_4[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang3_4[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang3_4[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang3_4[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang3_4[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang3_4[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta3_5 = np.array([[0,0,0,-0.004286],\
                      [0,0,0,+0.02],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint3_5 = forward_array + delta3_5
                waypoint_ang3_5 = project_helper_func.inverseKin(waypoint3_5,waypoint_ang3_4)
                for i in range(0,len(waypoint_ang3_5)):
                    while abs(waypoint_ang3_5[i])>np.pi*2:
                        waypoint_ang3_5[i]=(abs(waypoint_ang3_5[i])-np.pi*2)*waypoint_ang3_5[i]/abs(waypoint_ang3_5[i])

                print('waypoint_ang3=',waypoint_ang3_5)
                print('waypoint3=',waypoint3_5,'\n')
                print('calc_waypoint3=',project_helper_func.forward_ur3_kin(waypoint_ang3_5),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang3_5[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang3_5[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang3_5[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang3_5[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang3_5[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang3_5[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta3_6 = np.array([[0,0,0,0],\
                      [0,0,0,+0.02],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint3_6 = forward_array + delta3_6
                waypoint_ang3_6 = project_helper_func.inverseKin(waypoint3_6,waypoint_ang3_5)
                for i in range(0,len(waypoint_ang3_6)):
                    while abs(waypoint_ang3_6[i])>np.pi*2:
                        waypoint_ang3_6[i]=(abs(waypoint_ang3_6[i])-np.pi*2)*waypoint_ang3_6[i]/abs(waypoint_ang3_6[i])

                print('waypoint_ang3=',waypoint_ang3_6)
                print('waypoint3=',waypoint3_6,'\n')
                print('calc_waypoint3=',project_helper_func.forward_ur3_kin(waypoint_ang3_6),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang3_6[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang3_6[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang3_6[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang3_6[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang3_6[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang3_6[5],sim.simx_opmode_blocking)
                #time.sleep(1)

                delta4 = np.array([[0,0,0,0.0],\
                      [0,0,0,0.0171],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint4 = forward_array + delta4
                waypoint_ang4 = project_helper_func.inverseKin(waypoint4,waypoint_ang3_6)
                for i in range(0,len(waypoint_ang4)):
                    while abs(waypoint_ang4[i])>np.pi*2:
                        waypoint_ang4[i]=(abs(waypoint_ang4[i])-np.pi*2)*waypoint_ang4[i]/abs(waypoint_ang4[i])

                print('waypoint_ang4=',waypoint_ang4)
                print('waypoint4=',waypoint4,'\n')
                print('calc_waypoint4=',project_helper_func.forward_ur3_kin(waypoint_ang4),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang4[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang4[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang4[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang4[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang4[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang4[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta4_1 = np.array([[0,0,0,0.0],\
                      [0,0,0,0.01429],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint4_1 = forward_array + delta4_1
                waypoint_ang4_1 = project_helper_func.inverseKin(waypoint4_1,waypoint_ang4)
                for i in range(0,len(waypoint_ang4_1)):
                    while abs(waypoint_ang4_1[i])>np.pi*2:
                        waypoint_ang4_1[i]=(abs(waypoint_ang4_1[i])-np.pi*2)*waypoint_ang4_1[i]/abs(waypoint_ang4_1[i])

                print('waypoint_ang4=',waypoint_ang4_1)
                print('waypoint4=',waypoint4_1,'\n')
                print('calc_waypoint4=',project_helper_func.forward_ur3_kin(waypoint_ang4_1),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang4_1[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang4_1[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang4_1[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang4_1[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang4_1[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang4_1[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta4_2 = np.array([[0,0,0,0.0],\
                      [0,0,0,0.0114],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint4_2 = forward_array + delta4_2
                waypoint_ang4_2 = project_helper_func.inverseKin(waypoint4_2,waypoint_ang4_1)
                for i in range(0,len(waypoint_ang4_2)):
                    while abs(waypoint_ang4_2[i])>np.pi*2:
                        waypoint_ang4_2[i]=(abs(waypoint_ang4_2[i])-np.pi*2)*waypoint_ang4_2[i]/abs(waypoint_ang4_2[i])

                print('waypoint_ang4=',waypoint_ang4_2)
                print('waypoint4=',waypoint4_2,'\n')
                print('calc_waypoint4=',project_helper_func.forward_ur3_kin(waypoint_ang4_2),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang4_2[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang4_2[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang4_2[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang4_2[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang4_2[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang4_2[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta4_3 = np.array([[0,0,0,0.0],\
                      [0,0,0,0.00857],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint4_3 = forward_array + delta4_3
                waypoint_ang4_3 = project_helper_func.inverseKin(waypoint4_3,waypoint_ang4_2)
                for i in range(0,len(waypoint_ang4_3)):
                    while abs(waypoint_ang4_3[i])>np.pi*2:
                        waypoint_ang4_3[i]=(abs(waypoint_ang4_3[i])-np.pi*2)*waypoint_ang4_3[i]/abs(waypoint_ang4_3[i])

                print('waypoint_ang4=',waypoint_ang4_3)
                print('waypoint4=',waypoint4_3,'\n')
                print('calc_waypoint4=',project_helper_func.forward_ur3_kin(waypoint_ang4_3),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang4_3[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang4_3[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang4_3[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang4_3[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang4_3[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang4_3[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta4_4 = np.array([[0,0,0,0.0],\
                      [0,0,0,0.00571],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint4_4 = forward_array + delta4_4
                waypoint_ang4_4 = project_helper_func.inverseKin(waypoint4_4,waypoint_ang4_3)
                for i in range(0,len(waypoint_ang4_4)):
                    while abs(waypoint_ang4_4[i])>np.pi*2:
                        waypoint_ang4_4[i]=(abs(waypoint_ang4_4[i])-np.pi*2)*waypoint_ang4_4[i]/abs(waypoint_ang4_4[i])

                print('waypoint_ang4=',waypoint_ang4_4)
                print('waypoint4=',waypoint4_4,'\n')
                print('calc_waypoint4=',project_helper_func.forward_ur3_kin(waypoint_ang4_4),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang4_4[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang4_4[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang4_4[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang4_4[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang4_4[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang4_4[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta4_5 = np.array([[0,0,0,0.0],\
                      [0,0,0,0.002857],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint4_5 = forward_array + delta4_5
                waypoint_ang4_5 = project_helper_func.inverseKin(waypoint4_5,waypoint_ang4_4)
                for i in range(0,len(waypoint_ang4_5)):
                    while abs(waypoint_ang4_5[i])>np.pi*2:
                        waypoint_ang4_5[i]=(abs(waypoint_ang4_5[i])-np.pi*2)*waypoint_ang4_5[i]/abs(waypoint_ang4_5[i])

                print('waypoint_ang4=',waypoint_ang4_5)
                print('waypoint4=',waypoint4_5,'\n')
                print('calc_waypoint4=',project_helper_func.forward_ur3_kin(waypoint_ang4_5),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang4_5[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang4_5[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang4_5[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang4_5[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang4_5[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang4_5[5],sim.simx_opmode_blocking)
                #time.sleep(1)
                delta4_6 = np.array([[0,0,0,0.0],\
                      [0,0,0,0.0],\
                      [0,0,0,0],\
                      [0,0,0,0]])
                waypoint4_6 = forward_array + delta4_6
                waypoint_ang4_6 = project_helper_func.inverseKin(waypoint4_6,waypoint_ang4_5)
                for i in range(0,len(waypoint_ang4_6)):
                    while abs(waypoint_ang4_6[i])>np.pi*2:
                        waypoint_ang4_6[i]=(abs(waypoint_ang4_6[i])-np.pi*2)*waypoint_ang4_6[i]/abs(waypoint_ang4_6[i])

                print('waypoint_ang4=',waypoint_ang4_6)
                print('waypoint4=',waypoint4_6,'\n')
                print('calc_waypoint4=',project_helper_func.forward_ur3_kin(waypoint_ang4_6),'\n')

                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,waypoint_ang4_6[0],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,waypoint_ang4_6[1],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,waypoint_ang4_6[2],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,waypoint_ang4_6[3],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,waypoint_ang4_6[4],sim.simx_opmode_blocking)
                return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,waypoint_ang4_6[5],sim.simx_opmode_blocking)
                #time.sleep(1)

        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,0,sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,0,sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,0,sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,0,sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,0,sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,0,sim.simx_opmode_blocking)
        #time.sleep(1)        
        processed_parts = processed_parts+1
        return_code = sim.simxSetIntegerSignal(clientID,'newpart',0,sim.simx_opmode_blocking)
        time.sleep(2)
        print('in loop')



















sim.simxAddStatusbarMessage(clientID,'End of Code',sim.simx_opmode_oneshot)
print('End of Code')
res = input('reset? y/n:')
#print(res)
if(res == 'y'or res ==1):
    if(torch_type=='S' or torch_type == 's'):
        theta = np.radians([90,0,0,0,0,0])
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,theta[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,theta[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,theta[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,theta[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,theta[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,theta[5],sim.simx_opmode_blocking)
        time.sleep(5)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_stick',0,sim.simx_opmode_blocking)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_mig',0,sim.simx_opmode_blocking)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_tig',0,sim.simx_opmode_blocking)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_close',0,sim.simx_opmode_blocking)
        time.sleep(5)
    elif(torch_type=='M' or torch_type == 'm'):
        theta = np.radians([90,45,-90,0,0,0])
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,theta[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,theta[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,theta[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,theta[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,theta[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,theta[5],sim.simx_opmode_blocking)
        time.sleep(5)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_stick',0,sim.simx_opmode_blocking)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_mig',0,sim.simx_opmode_blocking)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_tig',0,sim.simx_opmode_blocking)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_close',0,sim.simx_opmode_blocking)
        time.sleep(5)
    elif(torch_type=='T' or torch_type == 't'):
        theta = np.radians([90,60,-120,0,0,0])
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,theta[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,theta[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,theta[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,theta[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,theta[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,theta[5],sim.simx_opmode_blocking)
        time.sleep(5)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_stick',0,sim.simx_opmode_blocking)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_mig',0,sim.simx_opmode_blocking)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_tig',0,sim.simx_opmode_blocking)
        return_code = sim.simxSetIntegerSignal(clientID,'BaxterGripper_close',0,sim.simx_opmode_blocking)
        time.sleep(5)

    return_code,signal=sim.simxGetIntegerSignal(clientID,'released',sim.simx_opmode_blocking)
    while(signal!=1):
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,theta[0],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,theta[1],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,theta[2],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,theta[3],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,theta[4],sim.simx_opmode_blocking)
        return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,theta[5],sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint1,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint2,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint3,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint4,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint5,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetJointTargetPosition(clientID,UR3_joint6,0,sim.simx_opmode_blocking)
    return_code = sim.simxSetObjectParent(clientID,stick,-1,True,sim.simx_opmode_blocking)
    return_code = sim.simxSetObjectParent(clientID,mig,-1,True,sim.simx_opmode_blocking)
    return_code = sim.simxSetObjectParent(clientID,tig,-1,True,sim.simx_opmode_blocking)
    #return_code = sim.simxSetObjectPosition(clientID,POI,-1,[-0.2700,0.01,0.652],sim.simx_opmode_blocking)
    
    