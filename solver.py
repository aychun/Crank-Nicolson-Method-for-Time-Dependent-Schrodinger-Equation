from WaveFunction import WaveFunction
from TDSE_functions import *
from TDSE_plots import *

# potentials = ["Infinite Sqaure Well", "Harmonic Potential", "Double Well"]

w1 = WaveFunction(L / 5, potential="Infinite Sqaure Well")
w2 = WaveFunction(L / 5, potential="Harmonic Potential")
w3 = WaveFunction(L / 3, potential="Double Well")

w1.solve(N=3000, save_data=True)
w2.solve(N=4000, save_data=True)
w3.solve(N=6000, save_data=True)
