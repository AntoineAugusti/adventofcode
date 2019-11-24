import re


def parse_line(line):
    res = re.findall(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$", line)
    return map(int, res[0])


with open("input.txt") as f:
    lines = list(filter(None, f.read().split("\n")))

grid = [([0] * 1000) for x in range(1000)]

for line in lines:
    claim_id, xpos, ypos, width, heigth = parse_line(line)
    for y in range(ypos, ypos + heigth):
        for x in range(xpos, xpos + width):
            grid[x][y] += 1

overlaps = 0
for row in grid:
    overlaps += sum(i > 1 for i in row)

print(overlaps)

for line in lines:
    is_valid = True
    claim_id, xpos, ypos, width, heigth = parse_line(line)
    for y in range(ypos, ypos + heigth):
        for x in range(xpos, xpos + width):
            if grid[x][y] > 1:
                is_valid = False
    if is_valid:
        print(claim_id)
