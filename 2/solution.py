reports = []
with open('input.txt', 'r') as file:
    for line in file:
        reports.append([int(x) for x in line.split()])

def isSafe(report: list[int], fixed: bool) -> bool:
    prev = report[0]
    for curr in report[1:]:
        diff = curr - prev
        if not (1 <= diff <= 3):
            if fixed:
                return False
            else:
                fixed = True
                continue
        prev = curr
    return True

count = 0
for report in reports:
    if report[0] > report[-1]:
        report = report[::-1]
    if isSafe(report, False) or isSafe(report[1:], True):
        count += 1

print(count)

