# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 03:50:47 2025

The purpose of the code is to simulate a chemical reaction
(oxidation of hydrogen sulfide) to model energy yields in chemosynthesis.

@author: Tomi Wang :)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants:
# Initial H2S concentration: 100 (arbitrary units)
# Reaction rate constant: k = 0.3
# Time array: from 0 to 10 (100 steps)

def reaction(y, t, k):
    # Simple first-order reaction: d[H2S]/dt = -k * [H2S]
    H2S = y[0]
    dH2S_dt = -k * H2S
    return [dH2S_dt]

# Initial concentration of H2S (arbitrary units)
y0 = [100]
t = np.linspace(0, 10, 100)
k = 0.3  # Reaction rate constant

# Solve the differential equation
sol = odeint(reaction, y0, t, args=(k,))
H2S_conc = sol[:, 0]
energy_yield = k * H2S_conc  # Assume energy yield is proportional to reaction rate

# Plot concentrations and energy yield
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(t, H2S_conc, label='[H2S]')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Hydrogen Sulfide Concentration')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, energy_yield, label='Energy Yield', color='orange')
plt.xlabel('Time')
plt.ylabel('Energy Yield')
plt.title('Energy Yield from Chemosynthesis')
plt.legend()

plt.tight_layout()
plt.show()
"""
This code solves a differential equation to determine H₂S concentration over time,
calculates energy output, and plots both metrics.
"""