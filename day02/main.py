from collections import Counter
from itertools import combinations

with open("input.txt") as f:
    lines = f.read().split("\n")

count_3 = 0
count_2 = 0
for line in lines:
    counter = Counter(line)
    increment_2 = 0
    increment_3 = 0
    for k in counter.keys():
        if counter[k] == 2:
            increment_2 = 1
        if counter[k] == 3:
            increment_3 = 1
    count_2 += increment_2
    count_3 += increment_3

for line1, line2 in combinations(lines, 2):
    line1, line2 = [ord(l) for l in line1], [ord(l) for l in line2]
    res = [i - j for i, j in zip(line1, line2)]
    res = [l for l in res if l != 0]
    if len(res) == 1:
        print([chr(l) for l in line1], [chr(l) for l in line2])
