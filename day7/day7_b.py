import numpy as np

with open("day7.input") as f:
    positions = [int(x) for x in f.readline().split(",")]
positions = np.array(positions)

def cost(dx):
    n = np.abs(dx)
    # sum(n) = n(n+1)/2
    return n * (n+1)/2

xs = np.arange(np.min(positions), np.max(positions))
costs = np.array([np.sum(cost(positions-x)) for x in xs])

i_opt = np.argmin(costs)
x_min = xs[i_opt]
print(x_min, costs[i_opt])