#!/.venv/Scripts/activate

import numpy as np
import pyperclip as pc

inputFile = './01-12-2024/Joost/input.txt'
input = np.loadtxt(inputFile,dtype=int)
input.sort(axis=0)

#part 1
result = 0 
for a,b in input:
    result += abs(a-b)
print(result)
pc.copy(result)

#part 2
result = 0
unique, counts = np.unique_counts(input[:,1])
countDict = dict(zip(unique,counts))
for a in input[:,0]:
    if a in unique:
        result += (a * countDict[a])

print(result)
pc.copy(result)


