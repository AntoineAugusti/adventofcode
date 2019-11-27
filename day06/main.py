from collections import defaultdict

with open("input.txt") as f:
    lines = list(filter(None, f.read().split("\n")))

points = []
for line in lines:
    points.append(tuple(map(int, line.replace(" ", "").split(","))))

minX, maxX = min(x for x, _ in points), max(x for x, _ in points)
minY, maxY = min(y for _, y in points), max(y for _, y in points)


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


counts = defaultdict(int)
infinite = set()
for y in range(minY, maxY + 1):
    for x in range(minX, maxX + 1):

        distances = {}
        for i, (px, py) in enumerate(points):
            distances[i] = manhattan(x, y, px, py)

        sorted_distances = sorted(distances.values())
        if sorted_distances[0] < sorted_distances[1]:
            closest_point = min(distances, key=lambda key: distances[key])
            counts[closest_point] += 1
            # Points at the border will extend infinitely
            if x in [minX, maxX] or y in [minY, maxY]:
                infinite.add(closest_point)

for point in infinite:
    counts.pop(point)

print(max(counts.values()))
