"""**FATIQUE ANALYSIS**"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Given Experimental Data (MPa vs cycles)

stress = np.array([175, 125, 75, 35])   # MPa
cycles = np.array([2e5, 6e5, 2.5e6, 2e8])

# Convert to log scale

log_stress = np.log10(stress)
log_cycles = np.log10(cycles)

# 2. Fit Basquin Model

coeffs = np.polyfit(log_cycles, log_stress, 1)
b = coeffs[0]
a = 10**coeffs[1]

# Generate smooth curve

N = np.logspace(4, 9, 200)
S = a * (N ** b)

# 3. Simulated Stress History (from your dynamic model)

t = np.linspace(0, 10, 300)
acceleration = 1.5 * np.sin(2 * np.pi * 0.5 * t)

# Convert to stress (simplified)

mean_stress = 80   # MPa
dynamic_stress = mean_stress + 20 * acceleration

# 4. Miner’s Damage Calculation

damage = 0
for s in dynamic_stress:
    s = abs(s)
    Nf = (s / a) ** (1 / b)   # cycles to failure
    damage += 1 / Nf
print("Total Damage:", damage)

# 5. Plot S-N Curve

plt.figure()
plt.loglog(cycles, stress, 'o', label="Experimental Data")
plt.loglog(N, S, label="Fitted S-N Curve")
plt.xlabel("Number of Cycles (N)")
plt.ylabel("Stress (MPa)")
plt.title("Fatigue Life Prediction (S-N Curve)")
plt.grid()
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 1000, 200)
stress_cycle = 120 + 60*np.sin(time/40)

# Damage accumulation

damage = np.cumsum((stress_cycle/300)**3)

plt.figure()
plt.plot(time, damage)
plt.xlabel("Time")
plt.ylabel("Damage")
plt.title("Fatigue Damage Accumulation")
plt.grid()
plt.show()
