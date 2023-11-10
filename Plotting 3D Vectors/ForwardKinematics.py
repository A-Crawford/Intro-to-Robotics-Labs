import numpy as np

theta1  = np.radians(30)
theta2 = np.radians(50)
L0 = 0
L1 = L2 = 0.5

DH = np.array([[L0, 0, 0, theta1],
               [L1, 0, 0, theta2],
               [L2, 0, 0, 0]])

T0_1 = np.array([
                [np.cos(DH[0, 3]), -np.sin(DH[0,3]), 0, DH[0,0]],
                [np.sin(DH[0, 3]), np.cos(DH[0,3]), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

T1_2 = np.array([[np.cos(DH[1,3]), -np.sin(DH[0, 3]), 0, DH[1, 0]],
                 [np.sin(DH[1,3]), np.cos(DH[1,3]), 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]
                 ])

T2_3 = np.array([[np.cos(DH[2, 3]), -np.sin(DH[2, 3]), 0, DH[2, 0]],
                 [np.sin(DH[1, 3]), np.cos(DH[1, 3]), 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

T0_3 = T0_1.dot(T1_2).dot(T2_3)

print(T0_3)