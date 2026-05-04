"""**STRUCTURAL AND STRESS ANALYSIS**"""

import numpy as np
import matplotlib.pyplot as plt

# REALISTIC CATERPILLAR VALUES

force = np.linspace(50000, 170000, 100)  # N

# Lift arm geometry

width = 0.3       # m
thickness = 0.05  # m
area_lift = width * thickness

# Pivot pin geometry

pin_diameter = 0.08  # m
area_pin = np.pi * (pin_diameter/2)**2

# Stress

stress_lift = force / area_lift
stress_pin = force / area_pin

# Factor of Safety

yield_strength = 250e6
fos_lift = yield_strength / stress_lift
fos_pin = yield_strength / stress_pin

# Plot

plt.figure()
plt.plot(force/1000, stress_lift/1e6, label="Lift Arm Stress (MPa)")
plt.plot(force/1000, stress_pin/1e6, label="Pivot Pin Stress (MPa)")
plt.xlabel("Load (kN)")
plt.ylabel("Stress (MPa)")
plt.title("Real Caterpillar-Based Stress Analysis")
plt.legend()
plt.grid()
plt.show()

# FOS

plt.figure()
plt.plot(force/1000, fos_lift, label="Lift Arm FOS")
plt.plot(force/1000, fos_pin, label="Pivot Pin FOS")
plt.xlabel("Load (kN)")
plt.ylabel("Factor of Safety")
plt.title("Factor of Safety (Real Geometry)")
plt.legend()
plt.grid()
plt.show()
