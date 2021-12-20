pos_horiz = 0
depth = 0

with open("day2.input") as f:
	for line in f.readlines():
		command, value = line.split(" ")
		value = int(value)
		if command == "forward":
			pos_horiz += value
		elif command == "down":
			depth += value
		elif command == "up":
			depth -= value
		else:
			raise ValueError("Unknown command")

print(pos_horiz, depth)
print(pos_horiz*depth)