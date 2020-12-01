from input import input_string
#input_string = """1721
#979
#366
#299
#675
#1456"""

input_array = [int(i) for i in input_string.split()]

less = [i for i in input_array if i < 2020/2]
more = [i for i in input_array if i >= 2020/2]

total = 0
for i in less:
    for x in input_array:
        for y in input_array:
            if x + i + y == 2020:
                total = x * i * y

    if total != 0:
        break

print(total)
