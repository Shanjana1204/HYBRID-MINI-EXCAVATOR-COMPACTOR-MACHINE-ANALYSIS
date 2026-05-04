"""**PRODUCTIVITY & OPERATION PERFORMANCE**"""

import numpy as np
import matplotlib.pyplot as plt

# Time components (seconds)

dig = 7
lift = 6
transport = 10
dump = 5

# Traditional cycle

cycle_traditional = dig + lift + transport + dump

# Hybrid saves time (parallel operations)

efficiency_factor = 0.75
cycle_hybrid = cycle_traditional * efficiency_factor
print("Traditional Cycle Time:", cycle_traditional, "s")
print("Hybrid Cycle Time:", cycle_hybrid, "s")

# Plot

labels = ["Traditional", "Hybrid"]
values = [cycle_traditional, cycle_hybrid]
plt.figure()
plt.bar(labels, values, color = ['orange', 'green'])
plt.title("Cycle Time Comparison")
plt.ylabel("Time (seconds)")
plt.grid(axis='y')
plt.show()

# Bucket capacity (Caterpillar compact loader)

bucket_capacity = 0.8  # m³

# Cycles per hour

cycles_traditional = 3600 / cycle_traditional
cycles_hybrid = 3600 / cycle_hybrid
productivity_traditional = cycles_traditional * bucket_capacity
productivity_hybrid = cycles_hybrid * bucket_capacity
print("Traditional Productivity:", productivity_traditional, "m³/hr")
print("Hybrid Productivity:", productivity_hybrid, "m³/hr")

# Plot

plt.figure()
plt.plot([productivity_traditional, productivity_hybrid])
plt.xticks([0,1], ["Traditional", "Hybrid"])
plt.title("Productivity Comparison")
plt.ylabel("m³/hr")
plt.grid()
plt.show()
