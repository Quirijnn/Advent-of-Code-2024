#!/.venv/Scripts/activate

import pyperclip as pc
import re

inputFile = './03-12-2024/Joost/input.txt'

with open(inputFile) as f:
    content = f.readlines()

res = 0
for line in content:
    matches = re.findall('mul\(\d{1,3},\d{1,3}\)', line)
    for match in matches:
        digits = list(map(int, re.findall('\d{1,3}', match)))
        res += digits[0] * digits[-1]

print(res)
pc.copy(res)

#part 2

res = 0
enabled = True
for line in content:
    matches = re.findall('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
    for match in matches:
        if match == 'do()':
            enabled = True
        elif match == 'don\'t()':
            enabled = False
        elif enabled == True:
            digits = list(map(int, re.findall('\d{1,3}', match)))
            res += digits[0] * digits[-1] 

print(res)
pc.copy(res)
