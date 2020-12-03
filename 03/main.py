file = open("input")
input = file.read().split("\n")[:-1]
file.close()

slopes = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

trees = [0 for i in slopes]

for i, slope in enumerate(slopes):
    x = 0
    y = 0
    while y < len(input):
        if input[y][x] == "#":
            trees[i] += 1
        x += slope[0]
        y += slope[1]

        if x >= len(input[0]):
            x -= len(input[0])

total = 1
for i in trees:
    total *= i

print(total)
