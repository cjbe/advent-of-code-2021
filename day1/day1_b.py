import numpy as np

ns = []

with open("day1.input") as f:
	for line in f.readlines():
		n = int(line)
		ns.append(n)

n_averaged = []
for i in range(len(ns)-2):
	n_averaged.append(np.sum(ns[i:i+3]))
n_averaged = np.array(n_averaged)

n_increases = np.sum(n_averaged[1:] > n_averaged[:-1])

print(n_increases)