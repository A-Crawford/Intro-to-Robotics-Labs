import numpy as np
import matplotlib.pyplot as plt
import spatialmath as sp

Frame_A = np.eye(3)
print(Frame_A)

XA=Frame_A[:,0]
YA=Frame_A[:,1]
ZA=Frame_A[:,2]

Frame_B=sp.SE3.Rx(np.pi/4).R@sp.SE3.Ry(np.pi/4).R@sp.SE3.Rz(np.pi/4).R@Frame_A
print(Frame_B)

XB=Frame_B[:,0]
YB=Frame_B[:,1]
ZB=Frame_B[:,2]
