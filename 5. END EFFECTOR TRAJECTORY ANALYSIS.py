"""**END EFFECTOR TRAJECTORY ANALYSIS**"""

L1 = 3.5  # lift arm length
L2 = 1.5  # bucket link

x = L1*np.cos(np.radians(theta_arm)) + L2*np.cos(np.radians(theta_bucket))
y = L1*np.sin(np.radians(theta_arm)) + L2*np.sin(np.radians(theta_bucket))

plt.figure()
plt.plot(x, y, label="Bucket Path")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("End Effector Trajectory")
plt.legend()
plt.grid()
plt.show()

# Cooling coefficient

cooling_coeff = 0.02
mass_oil = 50       # kg
cp = 2000           # J/kg°C

time = np.linspace(0, 2000, 200)

# Assume avg heat input

Q = 4000  # Watts

temp_rise = (Q * time) / (mass_oil * cp)
temp = 25 + temp_rise
cooling = temp * np.exp(-cooling_coeff * time)

plt.figure()
plt.plot(time, temp, label="Without Cooling")
plt.plot(time, cooling, label="With Cooling")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Cooling System Performance")
plt.legend()
plt.grid()
plt.show()
