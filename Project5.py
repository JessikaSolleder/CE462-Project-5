import numpy as np
import matplotlib.pyplot as plt
from cmath import cos, sin, tan
from tkinter import simpledialog

# Constants
Ls = 40.02  # feet, see hand calcs in GitHub
Wm = 12966.48  # lb, see hand calcs in GitHub

c_mean = 45  # lb/ ft^2
c_cov = 0.3 # percent / 100
c_stnd_dev = c_mean * c_cov

height = 20  # feet
failure_plane_incline = 30  # degrees, alpha
slope_face_incline = 40  # degrees, beta
phi = 28  # degrees

gamma_mean = 120  # lb/ft^3
gamma_cov = 0.05 # percent / 100
gamma_stnd_dev = gamma_mean * gamma_cov

Fs = ((c_mean * Ls) + (Wm * cos*(failure_plane_incline) * tan(phi))) / (Wm * sin*(failure_plane_incline))

prob_failure = (4 * c_rand) / (gamma_rand * height)

# Prompt user to input number of simulations
num_simulations = simpledialog.askinteger("Input", "Enter number of simulations:")

# Initialize array to store factor of safety values
Fs_values = np.zeros(num_simulations)

# Perform simulations
for i in range(num_simulations):
    # Generate random values from a normal distribution for parameters that vary
    Ls_random = np.random.normal(Ls, 1)  # Assuming a standard deviation of 1 for simplicity
    Wm_random = np.random.normal(Wm, 1)
    
#######################################
    # Calculate factor of safety
#   Fs_values[i] = ?
##################################################

# Plot histogram
plt.hist(Fs_values, bins=5, edgecolor='black')
plt.title('Histogram of Factor of Safety')
plt.xlabel('Factor of Safety')
plt.ylabel('Frequency')
plt.show()
