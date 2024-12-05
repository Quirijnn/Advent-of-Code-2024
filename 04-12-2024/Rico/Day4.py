import numpy as np

with open("input.txt", "r") as f:
    text = f.read().strip().split('\n')

#Part 1

array = np.array([list(line) for line in text])

word = "XMAS"
xmas_count = 0
length = len(word)
rows = len(array)
cols = len(array[0])
directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

def check_xmas(x_cor, y_cor, x_dir, y_dir):
    for i in range(length):
        new_x_cor = x_cor + i * x_dir
        new_y_cor = y_cor + i * y_dir
        if not (0 <= new_x_cor < rows and 0 <= new_y_cor < cols):
            return False
        if array[new_x_cor][new_y_cor] != word[i]:
            return False
    return True

for i in range(rows):
    for j in range(cols):
        for x_dir, y_dir in directions:
            if check_xmas(i, j, x_dir, y_dir):
                xmas_count += 1

# print(xmas_count)

#Part 2

with open("input.txt", "r") as f:
    text2 = [line.strip() for line in f]

def check_x_shape(data, slices, variants):
    count = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            for direction in directions2:
                try:
                    word =  ''.join([data[y + dy][x + dx] for dx, dy in direction])

                    if word in variants:
                        count += 1
                except:
                    pass

    return count

directions2 = [((0, 0), (1, 1), (2, 2), (0, 2), (2, 0)),]

part2 = check_x_shape(text2, directions2, {'MASMS', 'SAMSM', 'MASSM', 'SAMMS'})

print(part2)