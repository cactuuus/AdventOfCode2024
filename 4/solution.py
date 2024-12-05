WORD = "XMAS"
DIRS = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
matrix = []

with open('input.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        matrix.append(row)

# part 1

rows, cols = len(matrix), len(matrix[0])
count = 0

def findWord(pos: tuple[int, int], dir: tuple[int, int]) -> bool:
    r, c = pos
    for i in range(len(WORD)):
        if not (0 <= r < rows and 0 <= c < cols and matrix[r][c] == WORD[i]):
            return False
        r += dir[0]
        c += dir[1]
    return True

for r in range(rows):
    for c in range(cols):
        if not matrix[r][c] == WORD[0]:
            continue
        for dir in DIRS:
            found = findWord((r, c), dir)
            count += 1 if found else 0

print(count)

# part 2

VALID = [("M", "S"), ("S", "M")]

def isXmas(pos: tuple[int, int]) -> bool:
    r, c = pos
    cross1 = (matrix[r-1][c-1], matrix[r+1][c+1])
    cross2 = (matrix[r-1][c+1], matrix[r+1][c-1])
    if cross1 in VALID and cross2 in VALID:
        return True
    return False

new_count = 0
for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if matrix[r][c] != "A":
            continue
        new_count += 1 if isXmas((r, c)) else 0

print(new_count)