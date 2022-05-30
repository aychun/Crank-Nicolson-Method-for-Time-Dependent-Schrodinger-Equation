import numpy as np
from scipy.constants import hbar, m_e

L = 1e-8  # length of box
sigma = L / 25  # standard deviation of initial wave function
kappa = 500 / L  # wavenumber

N = 3000  # number of time step
tau = 1e-18  # time step
T = N * tau  # duration
P = 1024  # number of spatial intervals

xRange = np.linspace(-L / 2, L / 2, P)  # spatial interval
