# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 03:25:20 2025

The purpose of the code is to simulate the evolution of organisms in a chemosynthetic ecosystem
using a genetic algorithm.

@author: Tomi Wang :)
"""

import random
import matplotlib.pyplot as plt

# Constants:
# POP_SIZE = 50 Population size
# GENERATIONS = 30 Number of generations to simulate
# MUTATION_RATE = 0.1 Probability of mutation per individual

# Parameters for the genetic algorithm
POP_SIZE = 50
GENERATIONS = 30
MUTATION_RATE = 0.1

# Create an organism with a random metabolism (0: sulfur-based, 1: methane-based)
# and a random adaptation score.
def create_individual():
    return {
        'metabolism': random.choice([0, 1]),
        'adaptation': random.uniform(0, 1)
    }

# Fitness function: if the environment is sulfur-rich, sulfur-based organisms do better.
def fitness(individual, vent_environment='sulfur'):
    if vent_environment == 'sulfur':
        return individual['adaptation'] if individual['metabolism'] == 0 else individual['adaptation'] * 0.5
    else:
        return individual['adaptation'] if individual['metabolism'] == 1 else individual['adaptation'] * 0.5

# Crossover: average the adaptation values and randomly select one of the parent’s metabolism.
def crossover(parent1, parent2):
    child = {
        'adaptation': (parent1['adaptation'] + parent2['adaptation']) / 2,
        'metabolism': random.choice([parent1['metabolism'], parent2['metabolism']])
    }
    return child

# Mutation: adjust the adaptation slightly with some probability.
def mutate(individual):
    if random.random() < MUTATION_RATE:
        individual['adaptation'] += random.uniform(-0.1, 0.1)
        individual['adaptation'] = max(0, min(1, individual['adaptation']))
    return individual

# Initialize a population of organisms
population = [create_individual() for _ in range(POP_SIZE)]
fitness_history = []

for gen in range(GENERATIONS):
    # Evaluate fitness for the current generation
    pop_fitness = [fitness(ind) for ind in population]
    fitness_history.append(sum(pop_fitness) / POP_SIZE)
    
    # Roulette wheel selection
    total_fit = sum(pop_fitness)
    selected = []
    for _ in range(POP_SIZE):
        pick = random.uniform(0, total_fit)
        current = 0
        for ind, fit_val in zip(population, pop_fitness):
            current += fit_val
            if current > pick:
                selected.append(ind)
                break
                
    # Create the next generation via crossover and mutation
    next_gen = []
    for i in range(0, POP_SIZE, 2):
        parent1 = selected[i]
        parent2 = selected[i+1] if i+1 < POP_SIZE else selected[0]
        child1 = mutate(crossover(parent1, parent2))
        child2 = mutate(crossover(parent1, parent2))
        next_gen.extend([child1, child2])
    population = next_gen[:POP_SIZE]

# Plot the average fitness over generations
plt.plot(fitness_history)
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.title('Evolution in a Chemosynthetic Ecosystem')
plt.show()

"""
This code initializes a population, calculates fitness, performs selection, crossover, and mutation,
and then plots the average fitness over generations.
"""