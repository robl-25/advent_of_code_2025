with open('input.txt') as f:
    rotations = []
    for r in f.readlines():
        rotation = int(r.strip().replace('L', '-').replace('R', '+'))
        rotations.append(rotation)

index = 50
count = 0

for rotation in rotations:
    index = (index + rotation) % 100

    count += (index == 0)

print(count)
