#Part 1

with open("location_ID.txt", "r") as file:
    list1, list2 = [], []
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1_sorted = sorted(list1)
list2_sorted = sorted(list2)

differences = [abs(first - second) for first, second in zip(list1_sorted, list2_sorted)]
total = sum(differences)

print(total)

#Part 2

similarity = 0

for number in list1_sorted:
    similarity += number * list2_sorted.count(number)

print(similarity)