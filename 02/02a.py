file = "day-2-input.txt"

entries = []
valid = 0

with open(file, "r") as f:
    for line in f:
        parts = line.split(" ")
        entries.append({
            "letter": parts[1].replace(":", ""),
            "min": int(parts[0].split("-")[0]),
            "max": int(parts[0].split("-")[1]),
            "password": parts[2].rstrip()
        })

for e in entries:
    count = e["password"].count(e["letter"])
    if count >= e["min"] and count <= e["max"]:
        valid += 1

print(valid)
