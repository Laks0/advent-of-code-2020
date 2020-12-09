f = open("input")
input = f.read().splitlines()
f.close()

def run(code):
    accumulator = 0

    executed = []
    i = 0
    while True:
        if i in executed:
            return 1, accumulator
        if i >= len(code):
            return 0, accumulator
        
        executed.append(i)

        cmd, arg = code[i].split(" ")
        arg = int(arg)

        if cmd == "acc":
            accumulator += arg
        if cmd == "jmp":
            i += arg
            continue

        i += 1

for i, line in enumerate(input):
    op = line[:3]
    if op == "acc":
        continue

    newinput = input.copy()
    if op == "jmp":
        newinput[i] = "nop" + line[3:]
    if op == "nop":
        newinput[i] = "jmp" + line[3:]

    exit, acc = run(newinput)
    if exit == 0:
        print(acc)
        break
