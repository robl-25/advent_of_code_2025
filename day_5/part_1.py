with open('input.txt') as f:
    ranges_str, ingredients_str = f.read().split('\n\n')

ranges = []

for l in ranges_str.strip().split('\n'):
    start, end = l.strip().split('-')
    ranges.append(range(int(start), int(end) + 1))

total = 0

for ingredient in ingredients_str.strip().split('\n'):
    ingredient = int(ingredient)

    if any(ingredient in r for r in ranges):
        total += 1

print(total)
