file = "day-6-input.txt"

total = 0

with open(file, "r") as f:
    entries = f.read().split("\n\n")

for e in entries:
    p = [c for c in e if c != "\n"]
    total += len(set(p))

print(total)
