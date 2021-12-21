import numpy as np

def read_input(file):
    with open(file) as f:
        ns = [int(x) for x in f.readline().split(",")]
    return ns

def evolve_timestep(fish_frequency):
    n_create = fish_frequency[0]
    fish_frequency = fish_frequency[1:] + [0]
    fish_frequency[6] += n_create
    fish_frequency[8] += n_create
    return fish_frequency

fish = read_input("day6.input")
fish_frequency = [0]*9
for c in fish:
    fish_frequency[c] += 1

for i in range(256):
    fish_frequency = evolve_timestep(fish_frequency)
print(np.sum(fish_frequency))