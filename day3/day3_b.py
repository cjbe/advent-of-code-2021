with open("day3.input") as f:
    bitstrings = [line.strip() for line in f.readlines()]

def find_most_common_bit(bitstrings, bit_index=0):
    n_true = 0
    for bitstring in bitstrings:
        if bitstring[bit_index] == "1":
            n_true += 1
    return n_true / len(bitstrings) >= 0.5

def filter_bitstrings(bitstrings, bit_index=0, bit_select=True):
    bitstrings = [bitstring  for bitstring in bitstrings 
                    if (bitstring[bit_index] != "1") ^ bit_select]
    return bitstrings

def find_string(bitstrings, most_common=True):
    bit_index = 0
    while len(bitstrings) > 1:
        bit_select = find_most_common_bit(bitstrings, bit_index)
        if not most_common:
            bit_select = not bit_select
        bitstrings = filter_bitstrings(bitstrings, bit_index, bit_select)
        bit_index += 1
    return int(bitstrings[0], 2)

x = find_string(bitstrings)
y = find_string(bitstrings, most_common=False)
print("Oxygen generator rating: ", x)
print("CO2 scrubber rating: ", y)
print(x*y)