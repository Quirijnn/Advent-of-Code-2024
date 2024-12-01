from pathlib import Path

def get_lists():
    filepath: Path = Path("Input/01-12-2024/input1.txt")
    file = open(filepath, "r")
    with file as f:
        data = f.readlines()

    lst1, lst2 = [], []

    for line in data:
        item1, item2 = line.split()
        lst1.append(item1)
        lst2.append(item2)

    lst1.sort()
    lst2.sort()

    lst1 = [int(item) for item in lst1]
    lst2 = [int(item) for item in lst2]

    return lst1, lst2

def exercise_1(lst1: list, lst2: list):
    result = sum([abs(a - b) for a, b in zip(lst1, lst2)])
    print(result)

def exercise_2(lst1: list, lst2: list):
    freq_dict_lst2 = {}
    for item in lst2:
        freq_dict_lst2[item] = freq_dict_lst2.get(item, 0) + 1
    result = sum([item * freq_dict_lst2.get(item, 0) for item in lst1])
    print(result)

    
if __name__ == "__main__":
    lst1, lst2 = get_lists()
    exercise_1(lst1, lst2)
    exercise_2(lst1, lst2)