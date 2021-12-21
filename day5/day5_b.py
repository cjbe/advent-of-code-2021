import numpy as np
from day5_a import read_input

def mark_map(density, line):
    axis_change = line[1]-line[0]
    for t in range(0, np.max(np.abs(axis_change))+1):
        point = line[0] + t*np.sign(axis_change)
        density[point[0], point[1]] += 1

lines, dims = read_input("day5.input")
density = np.zeros(dims)

for line in lines:
    mark_map(density, line)

print(density.transpose())

print(np.sum(density>=2))