from pathlib import Path

filepath: Path = Path("Input/02-12-2024/input2.txt")
file = open(filepath, "r")
with file as f:
    data = f.readlines()

#Exercise 1
print(sum([((all(True if (1 <= abs(int(line.split(" ")[index]) - int(line.split(" ")[index + 1])) <= 3) else False for index in range(len(line.split(" ")) - 1))) and (True if (([int(item) for item in line.split(" ")] == sorted([int(item) for item in line.split(" ")])) or ([int(item) for item in line.split(" ")] == sorted([int(item) for item in line.split(" ")])[::-1])) else False)) for line in data]))
#Exercise 2
print(sum([any(((all(True if (1 <= abs(int(lst[index]) - int(lst[index + 1])) <= 3) else False for index in range(len(lst) - 1))) and (True if ((lst == sorted(lst)) or (lst == sorted(lst)[::-1])) else False)) for lst in [[int(item) for item in line.split(" ")][:i] + [int(item) for item in line.split(" ")][i+1:]  for i in range(len(line.split(" ")))]) for line in data]))