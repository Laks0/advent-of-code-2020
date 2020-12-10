with open("input", "r") as f:
    str = f.read()

input = [int(i) for i in str.splitlines()]
input.append(0)

input.sort()
input.append(input[-1]+3)

diffs = {1:0, 2:0, 3:0}

for i, n in enumerate(input[:-1]):
    nxt = input[ i+1 ]

    diff = nxt - n

    diffs[diff] += 1

print(diffs[1]*diffs[3])
