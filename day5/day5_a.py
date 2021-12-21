import numpy as np

def read_input(file):
    lines = []
    dims = [0,0]
    with open(file) as f:
        for line in f.readlines():
            line = [np.array([int(x) for x in part.split(",")]) for part in line.split("->")]
            lines.append(line)

            for point in line:
                for i in range(2):
                    if point[i]+1 > dims[i]:
                        dims[i] = point[i]+1
    return lines, dims

def mark_map(density, line):
    changing_axes = np.abs(line[1]-line[0]) > 0
    if np.all(changing_axes):
        return

    axis_vals = [ point[changing_axes] for point in line]

    for t in range(np.min(axis_vals), np.max(axis_vals)+1):
        if changing_axes[0]:
            x,y = t, line[0][1]
        else:
            x,y = line[0][0], t
        density[x,y] += 1

if __name__ == "__main__":
    lines, dims = read_input("day5.input")
    density = np.zeros(dims)

    for line in lines:
        mark_map(density, line)

    print(density.transpose())

    print(np.sum(density>=2))