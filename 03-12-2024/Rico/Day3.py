import re

#Part 1

with open("input.txt", "r") as f:
    txt = f.read()

def mul(a,b):
    return a*b

mult = []

for entry in re.findall(r'mul\(\d+,\d+\)', txt):
    mult.append(eval(entry))


#Part 2

enabled = True
upd_mult = []

for entry in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", txt):
    if entry.startswith("mul") and enabled:
        upd_mult.append(eval(entry))
    elif entry.startswith("do("):
        enabled = True
    else:
        enabled = False

print(sum(mult), sum(upd_mult))