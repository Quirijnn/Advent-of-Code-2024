from functools import reduce

with open("Input/03-12-2024/input3.txt", "r") as f:
    data = f.read()

def get_valid_inputs(data: str, part_2: bool = False) -> dict:
    valid_input = {}
    for i, char in enumerate(data):
        if part_2:
            if data[i:i+4] == "do()":
                valid_input[i] = "do()"
            if data[i:i+7] == "don't()":
                valid_input[i] = "don't()"
        if char != "m":
            continue
        if i+7 > len(data) or data[i:i+4] != "mul(":
            continue
        valid = False
        for j in range(4):
            if ord('0') <= ord(data[i+j+4]) <= ord('9'):
                if j == 3:
                    valid = False
                continue
            if data[i+j+4] == ",":
                valid = True
                comma_index = i+j+4
                break
            else:
                break
        if not valid:
            continue
        for j in range(4):
            if comma_index + j + 1 > len(data):
                return valid_input
            if ord('0') <= ord(data[comma_index + j + 1]) <= ord('9'):
                if j == 3:
                    valid = False
                continue
            if data[comma_index + j + 1] == ")":
                valid = True
                right_brac_index = comma_index + j + 1
                valid_input[i] = data[i:right_brac_index+1]
                break
            else:
                break
    return valid_input

def mul(x, y):
    return x*y

def process_valid_inputs_ex_2_ordered(input):
    result = 0
    process = True
    for my_string in input:
        if my_string == "do()":
            process = True
        elif my_string == "don't()":
            process = False
        elif process:
            result += eval(my_string)
    return result

valid_inputs = get_valid_inputs(data)

#Either
print(sum(map(lambda x: eval(x), valid_inputs.values())))
#or    
print(sum(eval(my_string) for my_string in valid_inputs.values()))

valid_inputs_ex_2 = get_valid_inputs(data, part_2 = True)

valid_inputs_ex_2_ordered = map(lambda key: valid_inputs_ex_2[key], sorted(valid_inputs_ex_2.keys()))
print(process_valid_inputs_ex_2_ordered(valid_inputs_ex_2_ordered))







