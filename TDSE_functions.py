from TDSE_constants import *
from typing import Callable


def square_well(x=None) -> int:
    return 0


def harmonic_oscillator(x: float, m: float = m_e, w: float = 3e15) -> float:
    return 0.5 * m * w**2 * x**2


def double_well(x: float, x1: float = L / 4, v0: float = 6e-17) -> float:
    return v0 * (x**2 / x1**2 - 1) ** 2


# Discretized Hamiltonian
def get_Hamiltonian(potential: Callable, P: int = P):
    """
    Returns the discretized Hamiltonian given the <potential> function and
    <P> number of spatial intervals.
    """

    delta = L / P

    A = -(hbar**2) / (2 * m_e * delta**2)
    H = np.zeros((P, P))

    for i in range(P):
        for j in range(P):
            if i == j:
                B = potential((i + 1) * delta - L / 2) - 2 * A
                H[i][j] = B

            elif j == i - 1 or j == i + 1:
                H[i][j] = A
            else:
                H[i][j] = 0

    return H
