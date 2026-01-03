with open('input.txt') as f:
    batteries = [list(l.strip()) for l in f.readlines()]

total = 0

for bank in batteries:
    index, num1 = max(enumerate(bank[:-1]), key=lambda x: x[1])
    num2 = max(bank[index + 1:])

    total += int(num1 + num2)

print(total)
