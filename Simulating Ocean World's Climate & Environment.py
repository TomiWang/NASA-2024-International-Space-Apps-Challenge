# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 03:26:03 2025

The purpose of the code is to simulate temperature gradients, ocean currents,
and chemical concentrations around a hydrothermal vent.

@author: Tomi Wang :)
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants:
# nx, ny = 100, 100 Grid dimensions
# x, y range: 0 to 10 Coordinate limits
# Hydrothermal vent position: (vent_x, vent_y) = (5, 5)
# Temperature model: 100 at vent, decreases by 10 * distance, minimum = 20
# pH model: baseline 7, increases by 0.1 per unit distance
# Sulfur concentration: 50 at vent, decays as exp(-distance/2)
# Methane concentration: 30 at vent, decays as exp(-distance/3)

# Grid dimensions and coordinate system
nx, ny = 100, 100
x = np.linspace(0, 10, nx)
y = np.linspace(0, 10, ny)
X, Y = np.meshgrid(x, y)

# Hydrothermal vent placed at the center
vent_x, vent_y = 5, 5
distance = np.sqrt((X - vent_x)**2 + (Y - vent_y)**2)

# Temperature: highest near the vent and decreasing with distance
temperature = 100 - 10 * distance  
temperature[temperature < 20] = 20  # ambient floor

# Ocean currents: assume they flow down the temperature gradient (convection)
u = -np.gradient(temperature, axis=1)  # x-component
v = -np.gradient(temperature, axis=0)  # y-component

# Chemical concentrations (simple models)
pH = 7 + 0.1 * (distance)               # pH increases slightly with distance
sulfur = np.exp(-distance/2) * 50        # high near vent, decaying outward
methane = np.exp(-distance/3) * 30       # similar pattern for methane

# Plotting the results
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# Temperature map
cf1 = ax[0, 0].contourf(X, Y, temperature, cmap='inferno')
ax[0, 0].set_title('Temperature Gradient')
fig.colorbar(cf1, ax=ax[0, 0])
ax[0, 0].scatter([vent_x], [vent_y], color='cyan', marker='*', s=100, label='Vent')
ax[0, 0].legend()

# Ocean currents using quiver plot
q = ax[0, 1].quiver(X, Y, u, v, color='blue')
ax[0, 1].set_title('Ocean Currents')

# Sulfur concentration
cf2 = ax[1, 0].contourf(X, Y, sulfur, cmap='plasma')
ax[1, 0].set_title('Sulfur Concentration')
fig.colorbar(cf2, ax=ax[1, 0])

# Methane concentration
cf3 = ax[1, 1].contourf(X, Y, methane, cmap='viridis')
ax[1, 1].set_title('Methane Concentration')
fig.colorbar(cf3, ax=ax[1, 1])

plt.tight_layout()
plt.show()

"""
This code creates a grid, computes values based on distance from a central vent,
and visualizes temperature, sulfur, methane, and pH distributions using contour
and quiver plots.
"""