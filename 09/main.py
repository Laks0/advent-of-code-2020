f = open("input")
input = [int(i) for i in f.read().splitlines()]
f.close()

poolsize = 25
invalid = 0

for i, n in enumerate(input):
    if i < poolsize:
        continue
    pool = input[i-poolsize:i]
    n = n

    valid = False
    for p1i, p1 in enumerate(pool):
        p1 = p1
        for p2i, p2 in enumerate(pool):
            p2 = p2
            if p1i == p2i:
                continue
            if p1 + p2 == n:
                valid = True
                break
        if valid:
            break

    if not valid:
        invalid = n
        break

for i, first in enumerate(input):
    total = first
    secuence = [first]

    for last in input[i+1:]:
        total += last
        secuence.append(last)
        if total >= invalid:
            break

    if total == invalid:
        minimo = min(secuence)
        maximo = max(secuence)
        print(minimo, maximo, minimo + maximo)
