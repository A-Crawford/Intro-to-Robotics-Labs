import sympy as sy
from sympy import Matrix
import numpy as np

theta1 = sy.symbols('theta1')
theta2 = sy.symbols('theta2')

L0 = sy.symbols('L0')
L1 = sy.symbols('L1')
L2 = sy.symbols('L2')

DH = sy.Matrix(
    [
        [L0, 0, 0, theta1],
        [L1, 0, 0, theta2],
        [L2, 0, 0, 0]
    ]
)

T0_1 = sy.Matrix(
    [
        [sy.cos(DH[0, 3]), -sy.sin(DH[0, 3]), 0, DH[0, 0]],
        [sy.sin(DH[0, 3]), sy.cos(DH[0, 3]), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
)

T1_2 = sy.Matrix(
    [
        [sy.cos(DH[1, 3]), -sy.sin(DH[1,3]), 0, DH[1, 0]],
        [sy.sin(DH[1,3]), sy.cos(DH[1,3]), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
)

T2_3 = sy.Matrix(
    [
        [sy.cos(DH[2, 3]), -sy.sin(DH[2, 3]), 0, DH[2, 0]],
        [sy.sin(DH[2, 3]), sy.cos(DH[2,3]), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
)

T0_2 = T0_1 * T1_2
T0_3 = T0_1 * T1_2 * T2_3

simplified_T0_3 = sy.simplify(T0_1)
print(simplified_T0_3)

# Numerical represetnation

theta1_frac_pi = sy.pi / 6
theta2_frac_pi = 5 * sy.pi / 18

T0_3_subs = T0_3.subs({theta1:theta1_frac_pi, theta2: theta2_frac_pi, L0: 0, L1: 0.5, L2: 0.5})
print(T0_3_subs)


T0_3_numerical = np.array(T0_3_subs).astype(float)
print(T0_3_numerical)