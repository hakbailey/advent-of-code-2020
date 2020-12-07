file = "day-6-input.txt"

total = 0

with open(file, "r") as f:
    entries = f.read().split("\n\n")

for e in entries:
    count = len(e.rstrip().split("\n"))
    p = [c for c in e if c != "\n"]
    for i in set(p):
        if p.count(i) == count:
            total += 1

print(total)
