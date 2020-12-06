import math

def getid(passport):
    minrow = 0
    maxrow = 128

    for i in range(7):
        distance = maxrow - minrow 
        tomove = math.floor(distance/2)
        
        if passport[i] == "B":
            minrow += tomove
        if passport[i] == "F":
            maxrow -= tomove


    mincolumn = 0
    maxcolumn = 9
    for i in range(7, 10):
        distance = maxcolumn - mincolumn 
        tomove = math.floor(distance/2)

        if passport[i] == "R":
            mincolumn += tomove
        if passport[i] == "L":
            maxcolumn -= tomove

    return minrow * 8 + mincolumn

f = open("input")
input = f.read().splitlines()
f.close()

ids = []
for p in input:
    ids.append(getid(p))

totalseats = 127 * 8 + 8
myseat = 0

for i in range(totalseats):
    if ( not i in ids ) and i-1 in ids and i+1 in ids:
        myseat = i
        break

print(myseat)
