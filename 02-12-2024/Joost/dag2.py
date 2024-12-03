#!/.venv/Scripts/activate

import pyperclip as pc

def checkLine(numbers):
    #damp exception
    if len(numbers) > 2:
        diffDamp = numbers[0] - numbers[2]

    result = 0
    #either recursively go down or recursively go up
    diff = numbers[0] - numbers[1]
    if abs(diff) > 0 and abs(diff) < 4: 
        if diff < 0:
            result = checkUp(numbers[1:], False)
        elif diff > 0:
            result = checkDown(numbers[1:], False)
    
    if result == 1:
        return result

    #check if damp works
    if abs(diffDamp) > 0 and abs(diffDamp) < 4: 
        if diffDamp < 0:
            result = checkUp(numbers[2:], True)
        elif diffDamp > 0:
            result = checkDown(numbers[2:], True)
        
    if result == 1:
        return result

    #check if first wrong
    afterDampDiff = numbers[1] - numbers[2]
    if abs(afterDampDiff) > 0 and abs(afterDampDiff) < 4:
        if afterDampDiff < 0:
            return(checkUp(numbers[2:], True))
        elif afterDampDiff > 0:
            return(checkDown(numbers[2:], True))
    return 0

def checkDown(numbers, dampUsed):
    #bc
    if len(numbers) == 1:
        return 1
    #decreasing means i=0 > i=1
    diff = numbers[0] - numbers[1]

    #damp exception
    diffDamp = -1
    if not dampUsed and len(numbers) > 2:
        diffDamp = numbers[0] - numbers[2]
    
    #normal
    if diff > 0 and diff < 4:
        return checkDown(numbers[1:], dampUsed)
    
    #damp
    if diffDamp > 0 and diffDamp < 4:
        return checkDown(numbers[2:], True)
    
    #endDamp
    if not dampUsed and len(numbers) == 2:
        return 1
    
    return 0

def checkUp(numbers, dampUsed):
    #bc
    if len(numbers) == 1:
        return 1
    #increasing means i=0 < i=1
    diff = numbers[1] - numbers[0]

    #damp exception
    diffDamp = -1
    if not dampUsed and len(numbers) > 2:
        diffDamp = numbers[2] - numbers[0]
    
    if diff > 0 and diff < 4 :
        return checkUp(numbers[1:], dampUsed)
    
    #damp
    if diffDamp > 0 and diffDamp < 4:
        return checkUp(numbers[2:], True)
    
    #endDamp
    if not dampUsed and len(numbers) == 2:
        return 1
    
    return 0

inputFile = './02-12-2024/Joost/input.txt'

with open(inputFile) as f:
    content = f.readlines()

result = 0
for line in content:
    words = line.split()
    numbers = list(map(int, words))
    if(checkLine(numbers) == 1):
        print(numbers)
    result += checkLine(numbers)

print(result)
pc.copy(result)

