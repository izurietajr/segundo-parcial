#!/usr/bin/env python3

#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

import array
import random

import numpy
from tree import *
from functools import reduce
from copy import copy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools


A, B, C, D, E = "A", "B", "C", "D", "E"
arr = [A, B, C, D, E]
arr2 = copy(arr)
filename = "results.csv"

distances = [
    # A   B   C   D   E
    [ 0,  7,  9,  8, 20],
    [ 7,  0, 10,  4, 11],
    [ 9, 10,  0, 15,  5],
    [ 8,  4, 15,  0, 17],
    [20, 11,  5, 17,  0],
]

dist = lambda x, y: distances[arr2.index(x)][arr2.index(y)]

node = Node(arr[0])
tree(node, copy(arr))

print(node.nodes)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Attribute generator
toolbox.register("attr_bool", random.randint, 0, 1)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def log_to_file(filename, line):
    with open(filename, "a") as log_file:
        log_file.write(line + "\n")

def evalTravelerTree(individual):
    comb = get_combination_from_genome(node, individual, len(arr)) + [arr[0]]
    travel_sum = sum([dist(comb[i], comb[i+1]) for i in range(len(comb)-1)])
    print(f"combination: {'-'.join(comb)}, distance: {travel_sum}")
    log_to_file(filename, f"{'-'.join(comb)},{travel_sum}")

    return travel_sum,

toolbox.register("evaluate", evalTravelerTree)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():

    random.seed(64)

    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=30,
                                   stats=stats, halloffame=hof, verbose=True)

    return pop, log, hof

if __name__ == "__main__":
    main()
