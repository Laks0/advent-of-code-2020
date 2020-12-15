f = open("input")
input = f.read().splitlines()
f.close()

mask = ""
mem = {}

for line in input:
    cmd, arg = line.split(" = ")

    if cmd == "mask":
        mask = arg
        continue

    adress = cmd[4:-1]

    binarg = format(int(arg), "036b")
    maskedbin = ""

    for i, content in enumerate(binarg):
        if mask[i] != "X":
            maskedbin += mask[i]
        else:
            maskedbin += content

    mem[adress] = int(maskedbin, 2)

total = 0
for k in mem.keys():
    total += mem[k]

print("Parte 1:", total)

mask = ""
mem = {}

for line in input:
    cmd, arg = line.split(" = ")

    if cmd == "mask":
        mask = arg
        continue
    
    rawadress = format(int(cmd[4:-1]), "036b")

    maskedadress = ""
    for i, content in enumerate(rawadress):
        if mask[i] == "0":
            maskedadress += content
        else:
            maskedadress += mask[i]

    adresses = [""]

    for i, content in enumerate(maskedadress):
        adding = []
        for pi, prefix in enumerate(adresses):
            if content != "X":
                adresses[pi] += content
            else:
                adding.append(adresses[pi] + "1")
                adresses[pi] += "0"
        adresses += adding

    for ad in adresses:
        mem[int(ad, 2)] = int(arg)

total = 0
for k in mem.keys():
    total += mem[k]

print("Parte 2:", total)
