last = None
n_increases = 0
with open("day1.input") as f:
	for line in f.readlines():
		n = int(line)
		if last is not None:
			if n > last:
				n_increases += 1
		last = n
print(n_increases)