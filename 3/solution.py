import re

with open('input.txt', 'r') as file:
    file_content = file.read()

# part 1

nums = re.findall(r"mul\((\d+),(\d+)\)", file_content)

total = 0
for x, y in nums:
    total += int(x) * int(y)

print(total)

# part 2

matches = re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", file_content)

total = 0
enabled = True
for regex_match in matches:
    match regex_match.group(0):
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            x, y = regex_match.group(1, 2)
            print(x, y)
            total += int(x) * int(y) if enabled else 0

print(total)