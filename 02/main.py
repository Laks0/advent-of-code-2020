from input import input_string

input_list = [i for i in input_string.split("\n")]
rules = [i.split(":")[0] for i in input_list]
passwords = [i.split(":")[1] for i in input_list]

right = 0
for i, p in enumerate(passwords):
    letter = rules[i].split(" ")[1]
    least = int(rules[i].split("-")[0])
    most = int(rules[i].split("-")[1].split(" ")[0])

#    ammount = 0
#    for l in p:
#        if l == letter:
#            ammount += 1
#    if least <= ammount <= most:
#        right += 1
    if ( p[least] == letter ) ^ ( p[most] == letter ):
        right += 1


print(right)
