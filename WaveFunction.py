from __future__ import annotations
from TDSE_functions import *
from scipy import integrate
from typing import Union


class WaveFunction:

    x0: float
    psi0: float
    potential: str

    psi_list: list[np.ndarray[float]]
    time_list: list
    expected_pos_list: list

    def __init__(self, x0: float, potential: str = "Infinite Sqaure Well") -> None:
        self.x0 = x0
        self.psi0 = 1
        psi0 = self.get_normalization_constant()
        self.set_psi0(psi0)

        self.potential = potential

        self.psi_list = []
        self.time_list = []
        self.expected_pos_list = []

    def get_normalization_constant(self) -> float:

        f = lambda x: np.abs(self.InitialPsi(x)) ** 2

        I = integrate.quad(f, -L / 2, L / 2)[0]

        return np.sqrt(1 / I)

    def set_psi0(self, psi0: float) -> None:
        self.psi0 = psi0

    def InitialPsi(self, x: float) -> float:
        """
        Returns the initial condition of the wavefunction psi
        """
        return self.psi0 * np.exp(
            -((x - self.x0) ** 2) / (4 * sigma**2) + 1j * kappa * x
        )

    def solve(
        self, save_data: bool = True, load_data: Union[bool, str] = False
    ) -> None:

        IMatrix = np.identity(P)
        psi = self.InitialPsi(xRange)
        t = 0

        if self.potential == "Infinite Sqaure Well":
            hamiltonian = get_Hamiltonian(square_well)
        elif self.potential == "Harmonic Potential":
            hamiltonian = get_Hamiltonian(harmonic_oscillator)
        elif self.potential == "Double Well":
            hamiltonian = get_Hamiltonian(double_well)

        Lmatrix = IMatrix + 1j * tau / (2 * hbar) * hamiltonian
        Rmatrix = IMatrix - 1j * tau / (2 * hbar) * hamiltonian

        ####### MAIN LOOP #######

        if not load_data:

            nextInt = 1
            while t < T:

                psi = np.reshape(psi, newshape=(P, 1))

                self.psi_list.append(psi)
                self.time_list.append(t)
                self.expected_pos_list.append(self.get_expected_pos(psi))

                v = np.matmul(Rmatrix, psi)

                psi = np.matmul(np.linalg.inv(Lmatrix), v)

                t += tau

                if int((t / (T) * 100) // 1) == nextInt:
                    nextInt += 1
                    print("computing... {:.1f}%".format((t / T * 100)))

        if load_data:
            npzfile = np.load(f"{load_data}")
            self.psi_list = npzfile["psi_list"]
            self.time_list = npzfile["time_List"]
            self.expected_pos_list = npzfile["expected_post_list"]

        if save_data:
            np.savez(
                f"TDSE_data_{self.potential}",
                psi_list=self.psi_list,
                time_list=self.time_list,
                expected_post_list=self.expected_pos_list,
            )

    def get_expected_pos(self, psi: list) -> float:

        x = np.reshape(xRange, newshape=(len(xRange), 1))  # column vector of the xRange
        integrand = np.conjugate(psi) * x * psi

        integrand = np.reshape(integrand, newshape=(1, len(integrand)))

        I = integrate.simpson(integrand, xRange)

        return I / L
