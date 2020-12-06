f = open("input")
input = f.read()
f.close()

passports = [ s.replace("\n", " ") for s in input.split("\n\n")]

right = 0

needed = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
]

eyes = [ 
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
]

for p in passports:
    passed = True

    fields = {}

    for f in p.split():
        if len(f.split(":")) < 2:
            continue
        field, value = f.split(":")

        fields[field] = value

    for n in needed:
        if not n in fields.keys():
            passed = False
            break
    if not passed:
        continue

    if not 1920 <= int(fields["byr"]) <= 2002:
        continue
    if not 2010 <= int(fields["iyr"]) <= 2020:
        continue
    if not 2020 <= int(fields["eyr"]) <= 2030:
        continue

    height_unit = fields["hgt"][-2:]
    height_value = fields["hgt"][:-2]
    height_value = int(height_value)

    if height_unit == "cm":
        if not 150 < height_value < 193:
            continue
    elif height_unit == "in":
        if not 59 < height_value < 76:
            continue

    if fields["hcl"][0] != "#":
        continue
    color = fields["hcl"][1:]
    if len(color) != 6:
        continue
    for c in color:
        if not c in "0123456789abcdef":
            passed = False

    if not fields["ecl"] in eyes:
        continue

    if not len(fields["pid"]) == 9:
        continue

    if passed:
        right += 1

print(right)
