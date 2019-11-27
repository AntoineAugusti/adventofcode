from string import ascii_lowercase

with open("input.txt") as f:
    lines = list(filter(None, f.read().split("\n")))

string = lines[0]


def shorten_polymer(string):
    res = []
    for x in list(string):
        if len(res) > 0 and abs(ord(res[-1]) - ord(x)) == 32:
            res.pop()
        else:
            res.append(x)
    return res


print(len(shorten_polymer(string)))


min_val = len(string)
for letter in list(ascii_lowercase):
    tmp = string.replace(letter, "").replace(letter.upper(), "")
    val = len(shorten_polymer(tmp))
    if val < min_val:
        min_val = val

print(min_val)
