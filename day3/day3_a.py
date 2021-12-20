with open("day3.input") as f:
    bitstrings = [line.strip() for line in f.readlines()]

bit_counts = [0]*len(bitstrings[0])
for string in bitstrings:
    for i, bit in enumerate(string):
        if bit=="1":
            bit_counts[i] +=1 

gamma = 0
for i, count in enumerate(bit_counts[::-1]):
    if count > len(bitstrings)/2:
        gamma += 1<<i

print(gamma)
epsilon = (2**len(bit_counts)-1) ^ gamma
print(epsilon)
print(epsilon*gamma)