import numpy as np
import re
from typing import Union
import copy

def find_N_XMAS(xmas_data: Union[list, np.array]):
    return len(re.findall("XMAS", "".join(xmas_data)))

with open("Input/04-12-2024/Input4.txt", "r") as f:
    data = f.read().split()

my_list = [[char for char in line] for line in data]
my_arr = np.array(my_list)

N_rows = my_arr.shape[0]
N_cols = my_arr.shape[1]

#Exercise 1

XMAS_count = 0
for line in my_arr:
    XMAS_count += find_N_XMAS(line)
    XMAS_count += find_N_XMAS(line[::-1])

my_arr_transposed = my_arr.transpose()
for line in my_arr_transposed:
    XMAS_count += find_N_XMAS(line)
    XMAS_count += find_N_XMAS(line[::-1])

my_forward_rolled_arr = copy.deepcopy(my_arr)
for i, line in enumerate(my_forward_rolled_arr):
    my_forward_rolled_arr[i] = np.roll(line, i)

my_forward_rolled_arr_transposed = my_forward_rolled_arr.transpose()

for i, line in enumerate(my_forward_rolled_arr_transposed):
    XMAS_count += find_N_XMAS(line[:i+1])
    XMAS_count += find_N_XMAS(line[i+1:])
    XMAS_count += find_N_XMAS(line[:i+1][::-1])
    XMAS_count += find_N_XMAS(line[i+1:][::-1])

my_backward_rolled_arr = copy.deepcopy(my_arr)
for i, line in enumerate(my_backward_rolled_arr):
    my_backward_rolled_arr[i] = np.roll(line, -i)

my_backward_rolled_arr_transposed = my_backward_rolled_arr.transpose()

for i, line in enumerate(my_backward_rolled_arr_transposed):
    XMAS_count += find_N_XMAS(line[:N_rows - i])
    XMAS_count += find_N_XMAS(line[N_rows - i:])
    XMAS_count += find_N_XMAS(line[:N_rows - i][::-1])
    XMAS_count += find_N_XMAS(line[N_rows - i:][::-1])

print("XMAS_count: ", XMAS_count)

#Exercise 2

def is_xmas(row_idx, col_idx, my_arr):
    if ({my_arr[row_idx-1, col_idx-1], my_arr[row_idx+1, col_idx+1]}  == {"M", "S"} and
        {my_arr[row_idx-1, col_idx+1], my_arr[row_idx+1, col_idx-1]}  == {"M", "S"}):
        return True
    return False

x_mas_count = 0

for row_idx in range(1, N_rows-1):
    for col_idx in range(1, N_cols-1):
        if my_arr[row_idx, col_idx] != "A":
            continue
        x_mas_count += is_xmas(row_idx, col_idx, my_arr)

print("x_mas_count: ", x_mas_count)






