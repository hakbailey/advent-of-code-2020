import re

file = "day-4-input.txt"

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid = 0


def check_height(height):
    if height[-2:] == "cm":
        h = int(height[:-2])
        if h >= 150 and h <= 193:
            return True
    if height[-2:] == "in":
        h = int(height[:-2])
        if h >= 59 and h <= 76:
            return True
    return False


def check_hair(hair):
    if (
        hair[0] == "#" and
        len(hair[1:]) == 6 and
        re.match("[0-9|a-f]{6}", hair[1:])
    ):
        return True
    else:
        return False


with open(file, "r") as f:
    text = f.read()
    passports = text.split("\n\n")

for p in passports:
    fields = re.split(" |\n", p)
    data = {f.split(":")[0]: f.split(":")[1] for f in fields}
    if (
        all(key in data for key in keys) and
        (int(data["byr"]) >= 1920 and int(data["byr"]) <= 2002) and
        (int(data["iyr"]) >= 2010 and int(data["iyr"]) <= 2020) and
        (int(data["eyr"]) >= 2020 and int(data["eyr"]) <= 2030) and
        check_height(data["hgt"]) and
        check_hair(data["hcl"]) and
        data["ecl"] in eye_colors and
        re.match("[0-9]{9}", data["pid"]) and len(data["pid"]) == 9
    ):
        valid += 1

print(valid)
