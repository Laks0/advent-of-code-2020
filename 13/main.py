f = open("input")
input = f.read().splitlines()
f.close()

# PARTE 1 #

earlyest = int(input[0])
ids = {}
for i in input[1].split(","):
    if i != "x":
        ids[int(i)] = 0

currentbest = 0
for i in ids.keys():
    x = 1
    bustime = 0
    while bustime < earlyest:
        bustime = x * i
        x += 1
    ids[i] = bustime

    if currentbest == 0:
        currentbest = i
        continue

    if bustime < ids[currentbest]:
        currentbest = i

print("Parte 1:", currentbest * (ids[currentbest] - earlyest) )

# PARTE 2 #

ids = {}
offset = 0
first = 0
last = 0
for i in input[1].split(","):
    if i != "x":
        ids[int(i)] = offset
        if offset == 0:
            first = int(i)
        if int(i) > last:
            last = int(i)

    offset += 1

lastoffset = ids[last]
stamp = last
factor = last
while True:
    locked = []

    passed = True
    for id in ids.keys():
        if (stamp + ids[id] - lastoffset) % id == 0:
            locked.append(id)
        else:
            passed = False

    if passed:
        print("Parte 2:", stamp - lastoffset)
        break

    factor = 1
    for i in locked:
        factor *= i

    stamp += factor

