"""**SYSTEM AND LOAD ANALYSIS**"""

import numpy as np
import matplotlib.pyplot as plt

pressure = np.linspace(20e6, 35e6, 100)  # Pa
flow_rate = 0.002  # m³/s 

power_input = pressure * flow_rate

plt.figure()
loss_factor = 0.15  # 15% loss typical
power_loss = power_input * loss_factor
useful_power = power_input - power_loss
efficiency = useful_power / power_input * 100

plt.plot(pressure/1e6, power_input/1000, label="Input Power")
plt.plot(pressure/1e6, useful_power/1000, label="Useful Power")
plt.plot(pressure/1e6, efficiency, label="Efficiency (%)")
plt.plot(pressure/1e6, power_loss/1000, label="Loss Power")

plt.xlabel("Pressure (MPa)")
plt.ylabel("Values")
plt.title("Hydraulic System Performance")
plt.legend()
plt.grid()
plt.show()

# 1. Time

t = np.linspace(0, 10, 300)

# 2. Motion

velocity = 2 + 0.6 * np.sin(2 * np.pi * 0.5 * t)
acceleration = np.gradient(velocity, t)

# 3. Parameters

g = 9.81
bucket_mass = 1200
connector_mass = 500
roller_mass = 1735
total_mass = bucket_mass + connector_mass + roller_mass
bucket_dist = 1.2
connector_dist = 1.0
roller_dist = 1.4

# 4. Calculations

force = total_mass * (g + acceleration)
torque = (
    bucket_mass * (g + acceleration) * bucket_dist +
    connector_mass * (g + acceleration) * connector_dist +
    roller_mass * (g + acceleration) * roller_dist
)

# Pin stress

pin_diameter = 0.08
pin_area = np.pi * (pin_diameter / 2) ** 2
stress = force / pin_area

# 5. Plot 1: Load System

plt.figure()
plt.plot(t, force, label="Dynamic Force (N)", color='blue')
plt.plot(t, torque, label="Torque (Nm)", color='green')
plt.xlabel("Time (s)")
plt.ylabel("Load Values")
plt.title("Load Transmission in Linkage System")
plt.legend()
plt.grid()
plt.show()

