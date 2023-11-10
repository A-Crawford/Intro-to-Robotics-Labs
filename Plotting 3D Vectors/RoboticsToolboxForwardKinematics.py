import numpy as np
import roboticstoolbox as rtb
from spatialmath import SE3

theta1 = np.radians(0)
theta2 = np.radians(0)
L0 = 0
L1 = L2 = 0.5

DH_Table = [
    [0, 0, 0, theta1],
    [L1, 0, 0, theta2],
    [L2, 0, 0, 0,],
]

RTB_DH_Table = [
    [0, L0, 0, theta1],
    [0, L1, 0, theta2],
    [0, L2, 0, 0],
]

robot = rtb.SerialLink(
    [
        rtb.RevoluteDH(d=RTB_DH_Table[0][0], a=RTB_DH_Table[0][1], alpha=RTB_DH_Table[0][2], offset=RTB_DH_Table[0][3]),
        rtb.RevoluteDH(d=RTB_DH_Table[1][0], a=RTB_DH_Table[1][1], alpha=RTB_DH_Table[1][2], offset=RTB_DH_Table[1][3]),
        rtb.RevoluteDH(d=RTB_DH_Table[2][0], a=RTB_DH_Table[2][1], alpha=RTB_DH_Table[2][2], offset=RTB_DH_Table[2][3]),
    ],
    name="Planar2"
)

print(robot)

J1 = np.radians(30)
J2 = np.radians(50)
Transformation_Matrix = robot.fkine([J1, J2, 0])

print("Forward Kinematics: \n", Transformation_Matrix)