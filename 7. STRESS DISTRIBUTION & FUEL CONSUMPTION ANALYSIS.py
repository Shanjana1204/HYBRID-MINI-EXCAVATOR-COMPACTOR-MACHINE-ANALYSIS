"""**STRESS DISTRIBUTION & FUEL CONSUMPTION ANALYSIS**"""

import numpy as np
import matplotlib.pyplot as plt

# Create grid

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

# Stress distribution (higher near center)

stress = 1 / (X**2 + Y**2 + 0.1)

plt.figure()
plt.contourf(X, Y, stress, levels=50)
plt.title("FEA-like Stress Distribution (Pivot Region)")
plt.colorbar(label="Stress Intensity")
plt.xlabel("X")
plt.ylabel("Y")
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

# Plot A: Fuel Efficiency Comparison (Line Plot)

plt.subplot(2, 2, 1)
plt.plot(df['Time (min)'], df['Hybrid Fuel (L/h)'], label='Hybrid System', color='green', lw=2)
plt.plot(df['Time (min)'], df['Standard Diesel (L/h)'], label='Standard Diesel', color='red', linestyle='--')
plt.title('Fuel Consumption Analysis (Hybrid vs Diesel)')
plt.ylabel('Liters per Hour')
plt.legend()
