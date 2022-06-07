# Crank-Nicolson-Method-for-Time-Dependent-Schrodinger-Equation

Crank-Nicolsan method is used for numerically solving partial differential equations. 
This program implements the method to solve a one-dimensinal time-dependent Schrodinger Equation (TDSE)

$$i \hbar \frac{\partial \psi}{\partial t} = - \frac{\hbar}{2m}\frac{\partial^2\psi}{\partial x^2} + V\psi$$

and we will analyze the solutions for Infinite Sqaure Well $V(x)=0$, Harmonic Oscillator $V(x)=\frac{1}{2}m\omega^2x^2$, and Double Well $V(x)=V_0\left(\frac{x^2}{x^2_1} - 1\right)^2$

## File Description

`WaveFunction.py` contains a WaveFunction class that has methods to initialize, solve, and calculate the expected position $< x >$.

`TDSE_constants.py` and `TDSE_functions.py` contain required constants and helper functions for the TDSE.

`TDSE_plots.py` contains functions to generate plots of the real part of the wavefunction, the expected position, and an animated plot of the probability density over time.

`solver.py` initilizes three WaveFunctions with different potentials and solve the TDSE using the Crank-Nicolsan method. It will also save the solutions as `.npz` files in the same directory. 

`main.py` loads the saved solution data files and plots $\Re (\psi(x, t))$ at $t=0, \frac{1}{4}T, \frac{1}{2}T$, and $T$. Then plot the expected position of each wavefunction over $t$.

## Result

<!-- Real psi -->

<p align="center">
  <img src=https://user-images.githubusercontent.com/85460898/172269745-b5cb17bb-d838-48bc-b436-75ad996ecf9b.png />
</p>



<p align="center">
  <img src=https://user-images.githubusercontent.com/85460898/172269735-67759979-8446-476d-bbe2-620ef6d47852.png />
</p>


<p align="center">
  <img src=https://user-images.githubusercontent.com/85460898/172269728-0dd6aba6-a069-4c3b-b11b-9f6d046088ce.png />
</p>


<!-- Expected Pos -->

<p align="center">
  <img src=https://user-images.githubusercontent.com/85460898/172270553-6b91855c-38a0-491c-9722-6310c1cdc34e.png />
</p>


<p align="center">
  <img src=https://user-images.githubusercontent.com/85460898/172270550-fca39a31-85e1-4c41-90ae-1374de6baf4b.png />
</p>



<p align="center">
  <img src=https://user-images.githubusercontent.com/85460898/172270544-b7ce41d8-5e7f-4ba5-a78d-608a472e1b10.png />
</p>


<!-- PDF -->


https://user-images.githubusercontent.com/85460898/172270086-3acce548-3ec3-4337-8c16-93311c39a930.mp4


https://user-images.githubusercontent.com/85460898/172270431-a4701086-78a9-4527-a7ba-2868b76d6547.mp4


https://user-images.githubusercontent.com/85460898/172270435-53974481-9321-419d-858a-4c8cb6a5c273.mp4



## Analysis 

The [Ehrenfest theroem](https://en.wikipedia.org/wiki/Ehrenfest_theorem) tells us that, 

"For general systems, if the wave function is highly concentrated around a point $x_0$, then $V'\left(\left\langle x\right\rangle \right)$ and $\left\langle V'(x)\right\rangle$ will be almost the same, since both will be approximately equal to $V'(x_{0})$. In that case, the expected position and expected momentum will approximately follow the classical trajectories, at least for as long as the wave function remains localized in position"

### Infinite Square Well
We can observe that both $\Re(\psi(x))$ and $|\psi(x)|^2$ have centralized points, in which the amplitude is highest. This implies that we would be able to (or at least high chance of) identify the position of the particle at some given point in time, as we would be able to do in a classical trajectory. Looking at the expected position plots, we can see that the particle linearly moves towards the ’wall’ of the infinite well, then ’bounces’ off it, then linearly moves again. Before once again ’bouncing’ off the opposite ’wall’ of the infinite well.

We have a well-defined trajectory of the particle which corresponds to a trajectory of a classical particle under no external force. 

### Harmonic Potential
Similarly, we can observe the centralized points of the wavefunction and the probability density. The expected position also mimics the behaviour of a classical particle on a string.

### Double Well
Unlike the previous parts, it is really hard to identify the centralized point of the wavefunction. This is not something that we would expect from a classical particle and the plot of the expected position also illustrate its special *(quantum mechanical)* behaviour. The trajectory doesn't follow any particular motion and doesn't resemble any classical trajectory.






  
