with open('input.txt') as f:
    rotations = []
    for r in f.readlines():
        rotation = int(r.strip().replace('L', '-').replace('R', '+'))
        rotations.append(rotation)

index = 50
count = 0

for rotation in rotations:
    x = index + rotation
    count += abs(x) // 100

    if index != 0 and x <= 0:
        count += 1

    index = x % 100

print(count)
