from collections import defaultdict

a, b = [], []

with open('input.txt', 'r') as file:
    for line in file:
        nums = [int(x) for x in line.split()]
        a.append(nums[0])
        b.append(nums[1])

# part 1

a.sort()
b.sort()

tot_dist = 0
for i in range(len(a)):
    tot_dist += abs(a[i] - b[i])

print(tot_dist)


# part 2

frequency = defaultdict(int)
for num in b:
    frequency[num] += 1

score = 0
for num in a:
    score += num * frequency[num]

print(score)

