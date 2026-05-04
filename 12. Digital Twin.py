"""**DIGITAL TWIN**"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Machine parameters

mass = 2000  # kg (arm + attachment)
target_position = 2.5  # m
target_vibration = 0.00047  # m

# Thermal

oil_temp = 40  # initial °C

# Wear

wear = 0

# State variables

position = 0
velocity = 0
vibration = 0

Kp, Ki, Kd = 80, 10, 20
error_sum = 0
prev_error = 0
dt = 0.05

time_data = []
pos_data = []
vib_data = []
temp_data = []
wear_data = []

t = 0

def update(frame):
    global position, velocity, vibration, oil_temp, wear
    global error_sum, prev_error, t

    t += dt

    # POSITION CONTROL
    
    error = target_position - position
    error_sum += error * dt
    d_error = (error - prev_error) / dt

    control_force = Kp*error + Ki*error_sum + Kd*d_error

    acceleration = control_force / mass
    velocity += acceleration * dt
    position += velocity * dt

    prev_error = error

    # VIBRATION CONTROL
    
    vibration += 0.2 * (target_vibration - vibration)

    # THERMAL MODEL
    
    heat_input = abs(control_force) * 0.01
    oil_temp += (heat_input - 0.05*(oil_temp - 30)) * dt

    # WEAR MODEL
    
    wear += abs(control_force) * 1e-8 * dt

    # STORE DATA
    
    time_data.append(t)
    pos_data.append(position)
    vib_data.append(vibration)
    temp_data.append(oil_temp)
    wear_data.append(wear)

    # PLOT UPDATE
    
    plt.clf()

    plt.subplot(2,2,1)
    plt.plot(time_data, pos_data)
    plt.axhline(target_position, linestyle='--')
    plt.title("Position (m)")

    plt.subplot(2,2,2)
    plt.plot(time_data, vib_data)
    plt.axhline(target_vibration, linestyle='--')
    plt.title("Vibration (m)")

    plt.subplot(2,2,3)
    plt.plot(time_data, temp_data)
    plt.axhline(80, linestyle='--')
    plt.title("Oil Temp (°C)")

    plt.subplot(2,2,4)
    plt.plot(time_data, wear_data)
    plt.title("Wear")

    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), update, interval=50)
plt.show()
