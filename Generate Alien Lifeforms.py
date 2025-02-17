# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 03:48:43 2025

The purpose of the code is to procedurally generate and visualize diverse alien
lifeforms with various attributes.

@author: Tomi Wang :)
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants:
# Lifeform attribute ranges:
#   body_size: uniform between 0.5 and 5.0
#   metabolism_rate: uniform between 0.1 and 1.0
#   sulfur_tolerance: uniform between 0 and 1
#   methane_tolerance: uniform between 0 and 1

# Procedurally generate a lifeform with various attributes.
def generate_lifeform():
    # Attributes include body_size, metabolism_rate, and tolerances
    return {
        'body_size': np.random.uniform(0.5, 5.0),
        'metabolism_rate': np.random.uniform(0.1, 1.0),
        'sulfur_tolerance': np.random.uniform(0, 1),
        'methane_tolerance': np.random.uniform(0, 1),
        'color': (np.random.rand(), np.random.rand(), np.random.rand())
    }

# Generate a small population of alien lifeforms
population = [generate_lifeform() for _ in range(10)]

# Visualize lifeforms: plot body size vs. metabolism rate with color coding
body_sizes = [lf['body_size'] for lf in population]
metab_rates = [lf['metabolism_rate'] for lf in population]
colors = [lf['color'] for lf in population]

plt.scatter(body_sizes, metab_rates, s=[size * 50 for size in body_sizes], c=colors)
plt.xlabel('Body Size')
plt.ylabel('Metabolism Rate')
plt.title('Procedurally Generated Alien Lifeforms')
plt.show()

# Placeholder for neural network generation:
# In practice, you might train a GAN or other generative model on environmental data.
def neural_network_generate(features):
    # Simulate slight variations using a neural network’s output
    return {key: val + np.random.normal(0, 0.1) for key, val in features.items()}

# Evolutionary mutation example
def mutate_lifeform(lifeform):
    mutated = lifeform.copy()
    for key in ['body_size', 'metabolism_rate', 'sulfur_tolerance', 'methane_tolerance']:
        mutated[key] += np.random.normal(0, 0.05)
        mutated[key] = max(0, mutated[key])
    return mutated

# Example: mutate the population to create variation
new_population = [mutate_lifeform(lf) for lf in population]

"""
This code randomly assigns traits like body size and metabolism rate to lifeforms,
plots them, and includes functions to simulate neural network variations and mutations.
"""