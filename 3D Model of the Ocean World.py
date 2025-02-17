# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 03:07:25 2025

The purpose of the code is to generate a 3D terrain map of the ocean world
and animate the dispersal of chemicals from a hydrothermal vent.

@author: Tomi Wang :)
"""

# Constants:
# nx, ny = 100, 100 Grid dimensions for terrain
# x, y range: -5 to 5 Coordinate limits for terrain
# Terrain model: Z = sin(sqrt(X^2 + Y^2)) * 2 (undersea mountains amplitude = 2)
# Hydrothermal vent: at (0, 0) with elevation 2
# Chemical plume: radius expands as 0.1 * frame, vertical oscillation amplitude 0.5, oscillation frequency factor 0.1

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Create a grid for terrain
nx, ny = 100, 100
x = np.linspace(-5, 5, nx)
y = np.linspace(-5, 5, ny)
X, Y = np.meshgrid(x, y)
# Use sine waves to simulate undersea mountains
Z = np.sin(np.sqrt(X**2 + Y**2)) * 2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='terrain', alpha=0.8)
ax.set_title('3D Terrain Map of Ocean World')
ax.set_xlabel('X coordinate')
ax.set_ylabel('Y coordinate')
ax.set_zlabel('Depth')

# Mark the hydrothermal vent (placed at the center, at a higher elevation)
ax.scatter(0, 0, 2, color='red', s=100, label='Hydrothermal Vent')
ax.legend()

# Animate a dispersing chemical plume from the vent
scatter = ax.scatter([0], [0], [2], color='blue', s=50)

def update(frame):
    # Create a circle that expands over time to simulate dispersion
    theta = np.linspace(0, 2*np.pi, 100)
    radius = 0.1 * frame
    plume_x = radius * np.cos(theta)
    plume_y = radius * np.sin(theta)
    plume_z = 2 + np.sin(theta * frame * 0.1) * 0.5  # adding vertical oscillation
    # Remove the previous plume and draw a new one
    ax.collections.remove(scatter)
    new_scatter = ax.scatter(plume_x, plume_y, plume_z, color='blue', s=20)
    return new_scatter,

ani = animation.FuncAnimation(fig, update, frames=50, interval=200, blit=False)
plt.show()

"""
This code builds a 3D surface using sine functions for terrain, marks the vent
location, and animates an expanding chemical plume with a scatter plot.
"""