"""**SOIL INTERACTION & COMPACTION ANALYSIS**"""

import numpy as np
import matplotlib.pyplot as plt

# Centrifugal force

F = 13600  # N

# Soil stiffness range

k = np.linspace(1e6, 5e7, 100)

# Depth estimation

depth = F / k

# Drum geometry

width = 1.0
diameter = 0.575
radius = diameter / 2

# Contact area (approx rectangular)

contact_length = 0.1   # m (typical contact patch)
area = width * contact_length

pressure = F / area

print("Contact Pressure:", pressure/1e6, "MPa")

passes = np.arange(1, 15)

eff = 100 * (1 - np.exp(-0.35 * passes))

plt.figure()

plt.plot(force/1000, depth, label="Depth vs Force")
plt.plot(passes, eff/100, label="Efficiency Trend")

plt.xlabel("Input Variable")
plt.ylabel("Response")
plt.title("Combined Compaction Performance")
plt.legend()
plt.grid()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# 1. Setup Synthetic Data for CAT Hybrid Compactor/Excavator

# Simulating a 60-minute work cycle
np.random.seed(42)
time = np.linspace(0, 60, 100)
fuel_hybrid = 15 - (time * 0.05) + np.random.normal(0, 0.2, 100)
fuel_diesel = 15 - (time * 0.12) + np.random.normal(0, 0.3, 100)
compaction_force = np.random.uniform(12,14,100) # kN
bucket_load = np.random.uniform(0, 1.7, 100)    # yd3
hydraulic_pressure = 150 + (bucket_load * 20) + np.random.normal(0, 5, 100)

df = pd.DataFrame({
    'Time (min)': time,
    'Hybrid Fuel (L/h)': fuel_hybrid,
    'Standard Diesel (L/h)': fuel_diesel,
    'Compaction Force (kN)': compaction_force,
    'Bucket Load (yd3)': bucket_load,
    'Hydraulic Pressure (Bar)': hydraulic_pressure
})

# 2. Visualizations

plt.figure(figsize=(14, 10))
sns.set_style("whitegrid")

# Plot A: Compaction Consistency (Distribution Plot)

plt.subplot(2, 2, 3)
sns.histplot(df['Compaction Force (kN)'], kde=True, color='purple')
plt.title('Roller Compaction Force Distribution')
plt.xlabel('Force (kN) - Goal: 18-22kN')
