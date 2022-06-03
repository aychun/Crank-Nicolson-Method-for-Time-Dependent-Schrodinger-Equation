import matplotlib.pyplot as plt
from WaveFunction import *


def plot_real_psi(w: WaveFunction, save_fig=False) -> None:
    """
    Plot the real part of the wavefunction
    """
    fig, axs = plt.subplots(2, 2, sharex="all", sharey=False, figsize=(9, 4))

    axs[0, 0].plot(xRange, np.real(w.psi_list[0]))
    axs[0, 0].grid()
    axs[0, 0].set_title("$ \Re(\psi(x))$ $(t=0)$")
    axs[0, 0].set_ylabel("$\Re(\psi(x))$ [m$^{-1/2}$]")
    # axs[0, 0].set_xlabel("$x (m)$")

    axs[0, 1].plot(xRange, np.real(w.psi_list[len(w.psi_list) // 4]))
    axs[0, 1].grid()
    axs[0, 1].set_title("$ \Re(\psi(x))$ $(t=T/4)$")
    # axs[0, 1].set_ylabel("$\Re(\psi(x))$ [m$^{-1/2}$]")
    # axs[0, 1].set_xlabel("$x (m)$")

    axs[1, 0].plot(xRange, np.real(w.psi_list[len(w.psi_list) // 2]))
    axs[1, 0].grid()
    axs[1, 0].set_title("$ \Re(\psi(x))$ $(t=T/2)$")
    axs[1, 0].set_ylabel("$\Re(\psi(x))$ [m$^{-1/2}$]")
    axs[1, 0].set_xlabel("$x (m)$")

    axs[1, 1].plot(xRange, np.real(w.psi_list[-1]))
    axs[1, 1].grid()
    axs[1, 1].set_title("$ \Re(\psi(x))$ $(t=T)$")
    axs[1, 1].set_xlabel("$x (m)$")

    plt.suptitle(f"{w.potential}")

    plt.tight_layout()

    if save_fig:
        plt.savefig(f"Real_Psi_{w.potential}.png")

    plt.show()


def plot_expected_pos(w: WaveFunction, save_fig=False) -> None:
    """
    Plot the expected position of the Wavefunction over time
    """

    plt.figure()

    plt.plot(w.time_list, np.real(w.expected_pos_list))
    plt.title(f"Expected position of the {w.potential} $(L=10^{-8}m)$")
    plt.ylabel("$<X> / L $")
    plt.xlabel("Time (s)")

    if save_fig:
        plt.savefig(f"Expected_Pos_{w.potential}.png")

    plt.show()


def plot_animated_pdf(w: WaveFunction) -> None:
    """
    Plot the animated probability density function of the Wavefunction
    """

    frame_counter = 0
    for i in range(1, len(w.time_list) + 1, 3):
        frame_counter += 1
        if frame_counter % 10 == 0:
            plt.clf()
            plt.xlabel("$x(m)$")
            plt.ylabel("Probability density")
            plt.title(f"Probability density $|\psi(x)|^2$ of {w.potential}")
            plt.plot(xRange, np.abs(w.psi_list[i]) ** 2, "r")
            plt.axvline(-L / 2)
            plt.axvline(L / 2)
            plt.ylim((0, 9e9))
            plt.draw()
            plt.pause(0.01)

    plt.show()
