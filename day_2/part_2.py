def is_repeated(n):
    s = str(n)
    partial_s = ''

    if len(s) == 1:
        return False

    for index, digit in enumerate(s):
        if index >= len(s) / 2:
            return False

        partial_s += digit

        if s.count(partial_s) * len(partial_s) == len(s):
            return True


with open('input.txt') as f:
    ranges = [tuple(int(i) for i in r.split('-')) for r in f.read().strip().split(',')]

total = 0

for start, end in ranges:
    total += sum(i for i in range(start, end + 1) if is_repeated(i))

print(total)
