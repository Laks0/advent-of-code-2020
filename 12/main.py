import numpy as np

f = open("input")
input = f.read().splitlines()
f.close()

position = np.array([0,0])
direction = 0
# 0 = east, 1 = south, 2 = west, 3 = north

directions = {
        0:np.array([1,0]),
        1:np.array([0,-1]),
        2:np.array([-1,0]),
        3:np.array([0,1])
}

for line in input:
    instruction = line[:1]
    argument = int(line[1:])

    if instruction == "N":
        position += [0,argument]
        continue
    if instruction == "S":
        position += [0,-argument]
        continue
    if instruction == "E":
        position += [argument,0]
        continue
    if instruction == "W":
        position += [-argument,0]
        continue
    if instruction == "F":
        position += directions[direction] * argument
        continue

    rotationSign = 1
    if instruction == "L":
        rotationSign = -1

    direction += rotationSign * (argument / 90)
    direction %= 4

print("Part 1:", abs(position[0]) + abs(position[1]))

position = np.array([0,0])
waypoint = {"E":10, "S":0, "W":0, "N":1}

for line in input:
    instruction = line[:1]
    argument = int(line[1:])

    if instruction in ["W", "N", "E", "S"]:
        waypoint[instruction] += argument
        continue
    if instruction == "F":
        north = waypoint["N"] - waypoint["S"]
        east = waypoint["E"] - waypoint["W"]

        position += np.array([east, north]) * argument
        continue

    rotationSign = -1
    if instruction == "L":
        rotationSign = 1

    direction = (argument / 90) % 4 * rotationSign

    numpway = np.array([[ waypoint["N"], waypoint["E"]], [waypoint["W"], waypoint["S"]]])
    numpway = np.rot90(numpway, direction)

    waypoint = {"E":numpway[0][1], "S":numpway[1][1], "W":numpway[1][0], "N":numpway[0][0]}

print("Part 2:", abs(position[0]) + abs(position[1]))
