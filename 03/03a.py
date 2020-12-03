file = "day-3-input.txt"

entries = []
trees = 0
n = 0

with open(file, "r") as f:
    for line in f:
        entries.append(line.split(" ")[0].rstrip())

for e in entries:
    try:
        place = e[n]
    except IndexError:
        n = n - len(e)
        place = e[n]
    if place == "#":
        trees += 1
    n += 3

print(trees)
