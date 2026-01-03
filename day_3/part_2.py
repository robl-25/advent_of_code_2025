with open('input.txt') as f:
    batteries = [list(l.strip()) for l in f.readlines()]

total = 0

for bank in batteries:
    joltage = ''
    index = -1

    for i in range(11):
        start = index + 1
        end = -11 + i

        index, num = max(enumerate(bank[start:end]), key=lambda x: x[1])
        index += start
        joltage += num

    joltage += max(bank[index + 1:])
    total += int(joltage)

print(total)
