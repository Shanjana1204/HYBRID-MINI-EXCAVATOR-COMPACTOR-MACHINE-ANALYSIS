"""**STRESS AND THERMAL ANALYSIS**"""

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

# Plot A: Operational Correlation Heatmap

plt.subplot(2, 2, 4)
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='RdYlGn', fmt=".2f",
    annot_kws={"size": 4.5},   # <--- REDUCE THIS to shrink text
   # cbar=False,              # Optional: Hide color bar to save space
   # square=True,             # Forces cells to be perfect squares
    #linewidths=.5
            )

plt.title('Variable Correlation Matrix')
plt.tight_layout()
plt.show()

# Plot B: Load vs Hydraulic Stress (Scatter Plot)

plt.subplot(2, 2, 2)
sns.regplot(x='Bucket Load (yd3)', y='Hydraulic Pressure (Bar)', data=df, color='blue')
plt.title('Bucket Volume vs. Hydraulic System Stress')
plt.axhline(220, color='red', linestyle='--', label='Max Pressure Limit')

