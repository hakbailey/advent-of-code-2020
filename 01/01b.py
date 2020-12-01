from itertools import combinations

file = "day-1-input.txt"

entries = []
result = 0

with open(file, "r") as f:
    for line in f:
        entries.append(int(line))

combos = combinations(entries, 3)
for i in combos:
    if i[0] + i[1] + i[2] == 2020:
        result = i[0] * i[1] * i[2]
        print(result)
