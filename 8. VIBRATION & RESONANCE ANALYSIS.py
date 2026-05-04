"""**VIBRATION & RESONANCE ANALYSIS**"""

import numpy as np
import matplotlib.pyplot as plt

# Caterpillar-based vibration parameters

frequency = 57  # Hz (typical soil compactor)
amplitude = 0.00047  # meters (0.47 mm)
time = np.linspace(0, 1, 1000)

# Vibration displacement

displacement = amplitude * np.sin(2 * np.pi * frequency * time)

# Plot

plt.figure()
plt.plot(time, displacement, label="Drum Vibration")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Roller Vibration Signal (Real Caterpillar Data)")
plt.legend()
plt.grid()
plt.show()

frequency = 32  # Hz (typical soil compactor)
amplitude = 0.00047  # meters (2.5 mm)
time = np.linspace(0, 0.5, 2000)

freq_range = np.linspace(1, 100, 300)
natural_freq = 15  # loader structure assumed

response = 1 / np.sqrt((natural_freq**2 - freq_range**2)**2 + (0.05*freq_range)**2)

plt.figure()
plt.plot(freq_range, response, label="System Response")
plt.axvline(x=frequency, linestyle='--', label="Operating Frequency (57 Hz)")
plt.axvline(x=natural_freq, linestyle='--', label="Natural Frequency (15 Hz)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude Response")
plt.title("Resonance Analysis")
plt.legend()
plt.grid()
plt.show()
