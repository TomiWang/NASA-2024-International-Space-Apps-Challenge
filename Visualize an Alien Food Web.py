# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 03:41:22 2025

Network Graph:
The purpose of the code is to visualize the predator-prey relationships
within an alien food web.

Population Dynamics:
The purpose of the code is to simulate and visualize the population
growth of different trophic levels.
    
@author: Tomi Wang :)
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Constants:
# Trophic levels (nodes): 'Chemosynthesizers', 'Grazers', 'Predators'
# Energy flow (edges): Chemosynthesizers -> Grazers, Grazers -> Predators
# Time array: 0 to 50 (100 points)
# Exponential growth rates:
#   Chemosynthesizers: initial pop = 50, growth rate = 0.05
#   Grazers: initial pop = 30, growth rate = 0.04
#   Predators: initial pop = 20, growth rate = 0.03

def plot_food_web():
    """
    Plots the alien food web as a directed graph.
    """
    # Define nodes (trophic levels) and edges (energy transfer)
    nodes = ['Chemosynthesizers', 'Grazers', 'Predators']
    edges = [('Chemosynthesizers', 'Grazers'), ('Grazers', 'Predators')]

    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # Generate positions for nodes using a spring layout
    pos = nx.spring_layout(G)

    # Create and display the graph
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=1500)
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    plt.title('Alien Food Web')
    plt.axis('off')
    plt.show()

def plot_population_dynamics():
    """
    Simulates and plots population dynamics for the alien food web.
    """
    # Simulate population growth over time using exponential models
    time = np.linspace(0, 50, 100)
    chemo_pop = 50 * np.exp(0.05 * time)    # population of primary producers
    grazer_pop = 30 * np.exp(0.04 * time)    # population of grazers
    predator_pop = 20 * np.exp(0.03 * time)   # population of predators

    # Create and display the population dynamics plot
    plt.figure(figsize=(8, 6))
    plt.plot(time, chemo_pop, label='Chemosynthesizers')
    plt.plot(time, grazer_pop, label='Grazers')
    plt.plot(time, predator_pop, label='Predators')
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.title('Population Dynamics in Alien Food Web')
    plt.legend()
    plt.show()

def main():
    """
    Main function to run the visualizations.
    """
    plot_food_web()
    plot_population_dynamics()

if __name__ == '__main__':
    main()

"""
A grazer is an organism that feeds on primary producers which in this case is
chemosynthesizers. They help transfer the energy produced by the chemosynthesizers
to higher levels of the food chain like predators.

Network Graph:
This code constructs a directed graph of trophic levels and energy flows using
NetworkX and displays it with a network layout.

Population Dynamics:
This code models exponential growth for chemosynthesizers, grazers, and predators,
and then plots their population dynamics over time.
"""