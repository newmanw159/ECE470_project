import scipy.linalg as linalg
import numpy as np
import math
'''
Input:  list of 6 joint angles
Output: Forward Kinemetics matrix
'''
def forward_ur3_kin(angles):
    T = []
    M =np.matrix([[1,0,0,-0.2700],\
                  [0,1,0,0.01],\
                  [0,0,1,0.652],\
                  [0,0,0,1]])
    W = [[0, -1, -1, -1,  0, -1],\
        [ 0,  0,  0,  0,  0,  0],\
        [ 1,  0,  0,  0,  1,  0]]
    '''
    using coppela measurements
    Q = [[0.00012,-0.1115,-0.1115,-0.1115,-0.1122,-0.1115],\
        [0.000086,0.000054,0.00013,0.000085,0.000085,0.000085],\
        [0.1045,0.1089,0.3525,0.5658,0.6500,0.6511]]
    '''
    #using lab measurements
    Q =[[0.0,-0.120,-0.120,-0.027,-0.110,-0.110],\
        [0.0, 0.0,   0.0,   0.0,   0.0,   0.0],\
        [0.0, 0.152, 0.396, 0.609, 0.609, 0.692]]

    V = [[0,0,0,0,0,0],\
        [0,0,0,0,0,0],\
        [0,0,0,0,0,0]]
    #v=cross(-w,q)
    for idx in range(0,6):
        V[0][idx]= -W[1][idx]*Q[2][idx]+W[2][idx]*Q[1][idx]
        V[1][idx]= -W[2][idx]*Q[0][idx]+W[0][idx]*Q[2][idx]
        V[2][idx]= -W[0][idx]*Q[1][idx]+W[1][idx]*Q[0][idx]

    S =[[W[0][0],W[0][1],W[0][2],W[0][3],W[0][4],W[0][5]],\
        [W[1][0],W[1][1],W[1][2],W[1][3],W[1][4],W[1][5]],\
        [W[2][0],W[2][1],W[2][2],W[2][3],W[2][4],W[2][5]],\
        [V[0][0],V[0][1],V[0][2],V[0][3],V[0][4],V[0][5]],\
        [V[1][0],V[1][1],V[1][2],V[1][3],V[1][4],V[1][5]],\
        [V[2][0],V[2][1],V[2][2],V[2][3],V[2][4],V[2][5]]]
    

    for joint in range(0,6):
        skew_S = [[0,            -1*S[2][joint],  S[1][joint],   S[3][joint]],\
                 [ S[2][joint],   0,             -1*S[0][joint], S[4][joint]],\
                 [-1*S[1][joint], S[0][joint],    0,             S[5][joint]],\
                 [ 0,             0,              0,             0]]
        T.append(linalg.expm((np.matrix(skew_S))*(angles[joint])))
    '''    
    for i in range(len(T)):
        print('T_',i,'\n',T[i],'\n')
    print(T[0]@T[1]@T[2]@T[3]@T[4]@T[5])
    '''
    T_final = T[0]@T[1]@T[2]@T[3]@T[4]@T[5]@M
    return(T_final)