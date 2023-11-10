import math
import numpy as np

def Euler_Angles(Transformation_matrix):
    Rotational_matrix = Transformation_matrix[:3, :3]

    roll = math.atan2(Rotational_matrix[2, 1], Rotational_matrix[2, 2])

    pitch = math.atan2(-Rotational_matrix[2, 0], (Rotational_matrix[2, 1] + Rotational_matrix[2, 2]))

    yaw = math.atan2(Rotational_matrix[1, 0], Rotational_matrix[0, 0])


    roll_deg = math.degrees(roll)
    pitch_deg = math.degrees(pitch)
    yaw_deg = math.degrees(yaw)

    return roll_deg, pitch_deg, yaw_deg

T0_3 = np.array([
    [0.1736, -0.9848, 0, 0.1736],
    [0.9848, 0.1736, 0, 00.9848],
    [0,     0,      1,      0],
    [0, 0, 0, 1]
])

print(T0_3)
[roll, pitch, yaw] = Euler_Angles(T0_3)
print('Roll angle: ', roll)
print('Pitch angle: ', pitch)
print('Yaw angle: ', yaw)