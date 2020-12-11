f = open("input")
position = f.read()
f.close()

def iterate(map):
    map = map.splitlines()
    map = [list(i) for i in map]
    newmap = [i.copy() for i in map]
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == ".":
                continue

            occupied = 0
            for dirx in range(-1,2):
                for diry in range(-1,2):

                    i = 1
                    while True:
                        checkx = dirx * i + x
                        checky = diry * i + y

                        if checkx >= len(row) or checkx < 0 or checky >= len(map) or checky < 0:
                            break

                        if map[checky][checkx] == "#":
                            occupied += 1
                        if map[checky][checkx] != ".":
                            break

                        i += 1

            if cell == "L" and occupied == 0:
                newmap[y][x] = "#"

            if cell == "#" and occupied >= 6:
                newmap[y][x] = "L"

    str = ["".join(i) for i in newmap]
    str = "\n".join(str)
    return str

while True:
    newmap = iterate(position)
    if position == newmap:
        break
    position = newmap

print(position.count("#"))

