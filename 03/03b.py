import math

file = "day-3-input.txt"
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

entries = []
trees = []

with open(file, "r") as f:
    for line in f:
        entries.append(line.split(" ")[0].rstrip())

for s in slopes:
    n = 0
    t = 0
    for i, e in enumerate(entries):
        if s[1] == 2 and i % 2 != 0:
            pass
        else:
            try:
                place = e[n]
            except IndexError:
                n = n - len(e)
                place = e[n]
            if place == "#":
                t += 1
            n += s[0]
    trees.append(t)

print(math.prod(trees))
