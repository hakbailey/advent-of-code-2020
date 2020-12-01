from itertools import combinations

file = "day-1-input.txt"

entries = []
result = 0

with open(file, "r") as f:
    for line in f:
        entries.append(int(line))

combos = combinations(entries, 2)
for i in combos:
    if i[0] + i[1] == 2020:
        result = i[0] * i[1]
        print(result)
