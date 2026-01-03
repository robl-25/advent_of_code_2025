from functools import cache


@cache
def is_repeated(n):
    s = str(n)

    if len(s) % 2 != 0:
        return False

    return s[:len(s) // 2] == s[len(s) // 2:]


with open('input.txt') as f:
    ranges = [tuple(int(i) for i in r.split('-')) for r in f.read().strip().split(',')]

total = 0

for start, end in ranges:
    total += sum(i for i in range(start, end + 1) if is_repeated(i))

print(total)
