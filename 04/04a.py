import re

file = "day-4-input.txt"

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0

with open(file, "r") as f:
    text = f.read()
    passports = text.split("\n\n")

for p in passports:
    fields = re.split(" |\n", p)
    data = {f.split(":")[0]: f.split(":")[1] for f in fields}
    if all(key in data for key in keys):
        valid += 1

print(valid)
