import re
from collections import Counter

with open("input.txt") as f:
    lines = list(filter(None, f.read().split("\n")))

lines = sorted(lines)
print(lines)

data = {}
guard_id = None


def find_minute(line):
    return int(re.search(r":(0?\d+)]", line).group(1))


most_common = None
max_value = 0
for line in lines:
    if "Guard #" in line:
        search = re.search(r"#(\d+) begins shift$", line)
        guard_id = int(search.group(1))
        minute_start = None
        minute_end = None
    if "wakes up" in line:
        minute_end = find_minute(line)
        if guard_id not in data:
            data[guard_id] = Counter()
        data[guard_id] = data[guard_id] + Counter(range(minute_start, minute_end))
        sleep_size = len(list(data[guard_id].elements()))
        if sleep_size > max_value:
            most_common = guard_id
            max_value = sleep_size
    if "falls asleep" in line:
        minute_start = find_minute(line)

print(most_common, data[most_common].most_common(1))
