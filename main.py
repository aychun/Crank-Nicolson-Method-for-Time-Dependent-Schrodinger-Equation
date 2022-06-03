from WaveFunction import WaveFunction
from TDSE_functions import *
from TDSE_plots import *

# potentials = ["Infinite Sqaure Well", "Harmonic Potential", "Double Well"]

w1 = WaveFunction(L / 5, potential="Infinite Sqaure Well")
w2 = WaveFunction(L / 5, potential="Harmonic Potential")
w3 = WaveFunction(L / 3, potential="Double Well")

w1.load_data("data/TDSE_data_Infinite Sqaure Well.npz")
w2.load_data("data/TDSE_data_Harmonic Potential.npz")
w3.load_data("data/TDSE_data_Double Well.npz")

# plot the wavefunctions
plot_real_psi(w1, save_fig=True)
plot_real_psi(w2, save_fig=True)
plot_real_psi(w3, save_fig=True)

# plot the expected positions
plot_expected_pos(w1, save_fig=True)
plot_expected_pos(w2, save_fig=True)
plot_expected_pos(w3, save_fig=True)
