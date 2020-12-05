import math

file = "day-5-input.txt"

ids = []


def pick_half(half, r):
    dist = (r[1] - r[0])/2
    if half == "F" or half == "L":
        r[1] = r[1] - math.floor(dist)
    else:
        r[0] = r[0] + math.ceil(dist)
    return r


with open(file, "r") as f:
    passes = f.readlines()

for p in passes:
    p = p.rstrip()
    row = [0, 127]
    col = [0, 7]
    for c in p[:7]:
        row = pick_half(c, row)
    for c in p[7:]:
        col = pick_half(c, col)
    id = row[0] * 8 + col[0]
    ids.append(id)

ids.sort()
for i, id in enumerate(ids):
    try:
        if ids[i+1] != id + 1:
            print(id + 1)
    except IndexError:
        pass
