import re

input = open('input')

total = 0
passport = {}

def check():
    global total, passport

    if not all (k in passport for k in ("byr","iyr","eyr","hgt","hcl","ecl","pid")):
        return

    byr = int(passport["byr"])
    iyr = int(passport["iyr"])
    eyr = int(passport["eyr"])
    hgt1 = passport["hgt"][:-2]
    hgt2 = passport["hgt"][-2:]
    hcl = passport["hcl"]
    ecl = passport["ecl"]
    pid = passport["pid"]

    policy = [
        1920 <= byr <= 2002,
        2010 <= iyr <= 2020,
        2020 <= eyr <= 2030,
        (hgt2 == "cm" and 150 <= int(hgt1) <= 193) or (hgt2 == "in" and 59 <= int(hgt1) <= 76),
        re.match(r"^#[0-9a-f]{6}$", hcl),
        ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        re.match(r"^\d{9}$", pid)
    ]

    if all(policy):
        total += 1

for lines in input.read().split("\n\n"):
    for line in lines.split('\n'):
        line = line.strip()
        for part in line.split(' '):
            k,v = part.split(':')
            passport[k] = v
    check()
    passport = {}

print(total)
