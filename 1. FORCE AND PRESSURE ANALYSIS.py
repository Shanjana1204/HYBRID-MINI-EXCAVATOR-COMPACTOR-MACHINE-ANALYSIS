'FORCE AND PRESSURE ANALYSIS'

import numpy as np
import matplotlib.pyplot as plt

# 1. TIME DOMAIN

t = np.linspace(0, 10, 200)   # 10 seconds simulation

# 2. VEHICLE MOTION (UNEVENT TERRAIN)

velocity = 2 + 0.5 * np.sin(2 * np.pi * 0.5 * t)
acceleration = np.gradient(velocity, t)

# 3. MASS DATA (REALISTIC VALUES)

bucket_weight = 1500      # kg
material_load = 1800      # kg
roller_weight = 1800      # kg
total_mass = bucket_weight + material_load + roller_weight

# 4. SYSTEM PARAMETERS

g = 9.81                 # gravity (m/s²)
d = 1.4                  # load distance from pivot (m)
r_cyl = 0.5              # cylinder lever arm (m)

# 5. TORQUE CALCULATION

torque = total_mass * (g + acceleration) * d

# 6. CYLINDER FORCE

F_cyl = torque / r_cyl

# 7. RESULTS

print("Maximum Cylinder Force (N):", np.max(F_cyl))
print("Minimum Cylinder Force (N):", np.min(F_cyl))

# 9. PRESSURE CALCULATION

# Assume cylinder diameter
D = 0.14  # meters (140 mm)
area = (np.pi / 4) * D**2
pressure = F_cyl / area

print("Maximum Pressure (Pa):", np.max(pressure))
print("Maximum Pressure (bar):", np.max(pressure) / 1e5)

# 10. PLOT: CYLINDER FORCE VS TIME

plt.figure()
plt.plot(t, F_cyl)
plt.xlabel("Time (s)", color='purple')
plt.ylabel("Cylinder Force (N)")
plt.title("Hydraulic Cylinder Force vs Time")
plt.grid()
plt.show()

# 11. PLOT: PRESSURE VS TIME

plt.figure()
plt.plot(t, pressure, color='red')
plt.xlabel("Time (s)")
plt.ylabel("Pressure (Pa)")
plt.title("Hydraulic Pressure vs Time")
plt.grid()
