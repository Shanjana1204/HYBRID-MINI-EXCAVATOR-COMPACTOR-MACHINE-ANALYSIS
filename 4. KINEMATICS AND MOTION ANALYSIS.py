"""**KINEMATICS AND MOTION ANALYSIS**"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parameters

D_PIN = 80          # Pin Diameter in mm
MASS_ROLLER = 1735 # kg
MASS_BUCKET = 1200  # kg
PAYLOAD_MAX = 5120  # kg (3.2m3 * 1600kg/m3)
L_ARM = 3.5         # Arm length in meters
G = 9.81            # Gravity

# Analysis Functions

def get_shear_stress(payload_kg, angle_deg):
    total_force = (MASS_ROLLER + MASS_BUCKET + payload_kg) * G
    # Assuming double shear configuration (2 cross-sections)
    area = 2 * np.pi * ((D_PIN / 2000)**2)
    stress_pa = total_force / area
    return stress_pa / 1e6 # Return in MPa

# Generate Data

angles = np.linspace(-10, 60, 100)
stresses_empty = [get_shear_stress(0, a) for a in angles]
stresses_full = [get_shear_stress(PAYLOAD_MAX, a) for a in angles]

# Visualization

plt.figure(figsize=(12, 5))

# Plot 1: Range of Motion / Clearance

plt.subplot(1, 2, 2)
for a in [-10, 25, 50]:
    x = L_ARM * np.cos(np.radians(a))
    y = L_ARM * np.sin(np.radians(a))
    plt.plot([0, x], [0, y], 'o-', label=f'Angle {a}°')
    # Represent Roller as a circle below the arm end
    circle = plt.Circle((x-0.4, y-0.6), 0.4, color='gray', alpha=0.3)
    plt.gca().add_patch(circle)
plt.axhline(0, color='brown', lw=2, label='Ground')
plt.title('Kinematic Range & Roller Clearance')
plt.xlabel('Horizontal (m)')
plt.ylabel('Vertical (m)')
plt.axis('equal')
plt.legend()
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()

time = np.linspace(0, 10, 200)

# Angles (realistic motion)

theta_arm = 30*np.sin(time)      # Lift arm
theta_bucket = 20*np.cos(time)   # Bucket
theta_roller = 10*np.sin(2*time) # Roller

plt.figure()
plt.plot(time, theta_arm, label="Lift Arm")
plt.plot(time, theta_bucket, label="Bucket")
plt.plot(time, theta_roller, label="Roller")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.title("Multi-Body Motion")
plt.legend()
plt.grid()
plt.show()
