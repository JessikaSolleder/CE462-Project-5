import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import simpledialog

# Constants
Ls = 40.02  # feet, see hand calcs in GitHub
Wm = 12966.48  # lb, see hand calcs in GitHub

c_mean = 45  # lb/ ft^2
c_cov = 0.3  # percent / 100
c_stnd_dev = c_mean * c_cov

height = 20  # feet
failure_plane_incline = 30  # degrees, alpha
slope_face_incline = 40  # degrees, beta
phi = 28  # degrees

gamma_mean = 120  # lb/ft^3
gamma_cov = 0.05  # percent / 100

gamma_stnd_dev = gamma_mean * gamma_cov

# Prompt user to input number of simulations
num_simulations = simpledialog.askinteger("Input", "Enter number of simulations:")

# Initialize array to store factor of safety values
Fs_values = np.zeros(num_simulations)

# Initialize counter for number of occurrences where Fs < 1.0
num_failures = 0

# Perform simulations
for i in range(num_simulations):
    # Generate random values from a normal distribution for parameters that vary
    c_rand = np.random.normal(c_mean, c_stnd_dev)
    gamma_rand = np.random.normal(gamma_mean, gamma_stnd_dev)
    
    # Calculate factor of safety
    Fs = ((c_rand * Ls) + (Wm * math.cos(math.radians(failure_plane_incline)) * math.tan(math.radians(phi)))) / (Wm * math.sin(math.radians(failure_plane_incline)))
    Fs_values[i] = Fs.real  # Take the real part of Fs
    
    # Check if Fs is less than 1.0
    if Fs < 1.0:
        num_failures += 1

# Calculate percentage of simulations where Fs < 1.0
failure_percentage = (num_failures / num_simulations) * 100

# Plot histogram
plt.hist(Fs_values, bins=20, edgecolor='black')
plt.title('Histogram of Factor of Safety')
plt.xlabel('Factor of Safety')
plt.ylabel('Frequency')
plt.show()

# Display final result in a pop-up box
result_message = f"Percentage of simulations with Fs < 1.0: {failure_percentage:.2f}%"
simpledialog.messagebox.showinfo("Simulation Results", result_message)
