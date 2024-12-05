from collections import defaultdict

adj_map = defaultdict(set)
updates = []

with open('input.txt', 'r') as file:
    # create adj_map
    while (line := file.readline()) != "\n":
        x, y = map(int, line.strip().split("|"))
        adj_map[x].add(y)
    # populates updates
    for line in file:
        update = list(map(int, line.strip().split(",")))
        updates.append(update[::-1])

def isValid(update: list[int]) -> bool:
    for i, x in enumerate(update):
        for y in update[i:]:
            if y in adj_map[x]:
                return False
    return True

answer = 0
for update in updates:
    if not isValid(update):
        continue
    mid = len(update) // 2
    answer += update[mid]

print(answer)

# part 2

def reOrder(update: list[int]) -> list[int]:
    while not isValid(update):
        order = {x: 0 for x in update}
        for i, x in enumerate(update):
            for y in update[i:]:
                if y in adj_map[x]:
                    order[x] += 1
        update.sort(key=lambda x: order[x])
    return update

answer = 0
for update in updates:
    if isValid(update):
        continue
    update = reOrder(update)
    mid = len(update) // 2
    answer += update[mid]
print(answer)