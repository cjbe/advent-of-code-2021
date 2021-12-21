def read_input(file):
    with open(file) as f:
        ns = [int(x) for x in f.readline().split(",")]
    return ns

def evolve_timestep(fish):
    n_create = 0
    for i, n in enumerate(fish):
        if fish[i] == 0:
            n_create +=1
            fish[i] = 6
        else:
            fish[i] -= 1
    fish.extend([8]*n_create)

fish = read_input("day6.input")
for i in range(80):
    evolve_timestep(fish)
print(len(fish))