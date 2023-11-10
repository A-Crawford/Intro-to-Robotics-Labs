import numpy as np
import roboticstoolbox as rtb
from spatialmath import SE3

L0 = 0
L1 = L2 = 0.5

SE3(x, 0, 0) * SE3.Rz == SE3.Trans(x, 0, 0) * SE3.Rot(0, 0, z)

Transformation_Matrix = SE3(L0, 0, 0) * SE3.Rz(30, 'deg') * SE3(L1, 0, 0) * SE3.Rz(50, 'deg') * SE3(L2, 0, 0) * SE3.Rz(0, 'deg')

T = Transformation_Matrix
print(T)