import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Frame_A = np.eye(3)
theta1=theta2=theta3=45

angle_x=angle_y=angle_z = np.radians(45)

def rotation_matrix_x(angle):
    cos = np.cos(angle)
    sin = np.sin(angle)
    return np.array([
        [1, 0, 0],
        [0, cos, -sin],
        [0, sin, cos]   
    ])

def rotation_matrix_y(angle):
    cos = np.cos(angle)
    sin = np.sin(angle)
    return np.array([
        [cos, 0, sin],
        [0, 1, 0],
        [-sin, 0, cos]
        ])

def rotation_matrix_z(angle):
    cos = np.cos(angle)
    sin = np.sin(angle)
    return np.array([
    [cos,-sin, 0],
    [sin, cos, 0],
    [0, 0, 1]
 ])

RotX = rotation_matrix_x(angle_x)
RotY = rotation_matrix_y(angle_y)
RotZ = rotation_matrix_z(angle_z)

Frame_B = RotX@RotY@RotZ
print('Frame_A',Frame_A)
print('\n')
print('Frame B', Frame_B)

XA = Frame_A[:,0]
YA = Frame_A[:,1]
ZA = Frame_A[:,2]

XB = Frame_B[:,0]
YB = Frame_B[:,1]
ZB = Frame_B[:,2]

# Lets make a 3D plot of the Vector frame
figure1 = plt.figure()
Xa = figure1.add_subplot(111, projection='3d') # This creates an instance of the 3D plot
Xa.quiver(0, 0, 0, XA[0], XA[1], XA[2], color='b') # Plots the vector XA with origin 0 in 3D space
Xa.text(XA[0], XA[1], XA[2], 'XA', color='b', fontsize=7)
# Adds the frame name to the vector XA
Xa.quiver(0, 0, 0, YA[0], YA[1], YA[2], color='b')
Xa.text(YA[0], YA[1], YA[2], 'YA', color='b', fontsize=7)
Xa.quiver(0, 0, 0, ZA[0], ZA[1], ZA[2], color='b')
Xa.text(ZA[0], ZA[1], ZA[2], 'ZA', color='b', fontsize=7)



# Propagating the Frame A to Frame B by rotating Frame A by 45 degrees about the X axis
Xa.quiver(0, 0, 0, XB[0], XB[1], XB[2], color='r') # Plots the vector XA with origin 0 in 3D space
Xa.text(XB[0], XB[1], XB[2], 'XB', color='r', fontsize=7) # Adds the frame name to the vector XA
Xa.quiver(0, 0, 0, YB[0], YB[1], YB[2], color='r')
Xa.text(YB[0], YB[1], YB[2], 'YB', color='r', fontsize=7)
Xa.quiver(0, 0, 0, ZB[0], ZB[1], ZB[2], color='r')
Xa.text(ZB[0], ZB[1], ZB[2], 'ZB', color='r', fontsize=7)

Xa.set_xlim([-1, 1])
Xa.set_ylim([-1, 1])
Xa.set_zlim([-1, 1])

Xa.set_xlabel('X')
Xa.set_ylabel('Y')
Xa.set_zlabel('Z')

Xa.set_title('Frame A and Frame B')

plt.show()

input('Press any key to continue')