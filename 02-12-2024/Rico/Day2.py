#Part 1

with open("input.txt", "r") as file:
    reports = [list(map(int, line.split())) for line in file]

safe = lambda x: (x == sorted(x) or x == sorted(x, reverse= True)) and all(1 <= abs(x[i + 1] - x[i]) <= 3 for i in range(len(x) - 1))

#Part 2

def dampener(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if safe(new_report):
            return True
    return False

def ultimate_safe_report(reports):
    return sum(1 for report in reports if safe(report) or dampener(report))




