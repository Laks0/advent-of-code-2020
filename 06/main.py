f = open("input")
input = f.read().split("\n\n")
f.close()

def getPositives(group):
    people = group.split("\n")
    positives = []

    for answer in people[0]:
        toappend = True
        for person in range(1, len(people)):
            toappend = toappend and answer in people[person]

        if toappend:
            positives.append(answer)

    return len(positives)

total = 0
for i in input:
    total += getPositives(i)

print(total)
