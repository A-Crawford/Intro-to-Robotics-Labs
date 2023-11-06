import numpy as np
import matplotlib.pyplot as plt
import spatialmath as sp
from mpl_toolkits.mplot3d import Axes3D

Frame_A = np.eye(3)
print('Frame A: \n', Frame_A)

XA=Frame_A[:,0]
YA=Frame_A[:,1]
ZA=Frame_A[:,2]

Frame_B = sp.SE3.Rz(np.radians(30)).R@Frame_A
XB=Frame_B[:,0]
YB=Frame_B[:,1]
ZB=Frame_B[:,2]
print('\n')
print('Freame B: \n', Frame_B)

figure1 = plt.figure()
Xa = figure1.add_subplot(111, projection='3d')

# Draw Frame A
Xa.quiver(0, 0, 0, XA[0], XA[1], XA[2], color='b')
Xa.text(XA[0], XA[1], XA[2], 'XA', color='b', fontsize=7)

Xa.quiver(0, 0, 0, YA[0], YA[1], YA[2], color='b')
Xa.text(YA[0], YA[1], YA[2], 'YA', color='b', fontsize=7)

Xa.quiver(0, 0, 0, ZA[0], ZA[1], ZA[2], color='b')
Xa.text(ZA[0], ZA[1], ZA[2], 'ZA', color='b', fontsize=7)

# Define origin of Frame B with respect to Frame A
AP = ([10, 5, 0])
Xa.quiver(AP[0], AP[1], AP[2], XB[0], XB[1], XB[2], color='r')
Xa.text(XB[0]+AP[0], XB[1]+AP[1], XB[2]+AP[2], 'XB', color='r', fontsize=7)

Xa.quiver(AP[0], AP[1], AP[2], YB[0], YB[1], YB[2], color='r')
Xa.text(YB[0]+AP[0], YB[1]+AP[1], YB[2]+AP[2], 'YB', color='r', fontsize=7)

Xa.quiver(AP[0], AP[1], AP[2], ZB[0], ZB[1], ZB[2], color='r')
Xa.text(ZB[0]+AP[0], ZB[1]+AP[1], ZB[2]+AP[2], 'ZB', color='r', fontsize=7)

Xa.quiver(0, 0, 0, AP[0], AP[1], AP[2], color='g')
Offset=0.04
Xa.text(AP[0]+Offset, AP[1]+Offset, AP[2]+Offset, 'AP', color='r', fontsize=7)

Xa.set_xlim([-2, 12])
Xa.set_ylim([-2, 12])
Xa.set_zlim([-2.5, 2.5])

Xa.set_xlabel('X')
Xa.set_ylabel('Y')
Xa.set_zlabel('Z')

Xa.set_title('Frame A and Frame B')

plt.show()