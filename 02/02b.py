file = "day-2-input.txt"

entries = []
valid = 0

with open(file, "r") as f:
    for line in f:
        parts = line.split(" ")
        entries.append({
            "letter": parts[1].replace(":", ""),
            "first": int(parts[0].split("-")[0]),
            "second": int(parts[0].split("-")[1]),
            "password": parts[2].rstrip()
        })

for e in entries:
    first = e["password"][e["first"]-1]
    second = e["password"][e["second"]-1]
    if (first + second).count(e["letter"]) == 1:
        valid += 1

print(valid)
