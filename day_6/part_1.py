import re
import operator

from pprint import pp
from functools import reduce


def enumerate_n(iterable, start=0, n=1):
    from collections.abc import Iterable

    count = start

    for item in iterable:
        if isinstance(item, Iterable) and n > 1:
            for index, value in enumerate_n(iter(item), start=start, n=n - 1):
                if not isinstance(index, Iterable):
                    index = [index]

                yield tuple([count, *index]), value
        else:
            yield count, item

        count += 1


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = []

    for _ in range(cols):
        transposed_matrix.append([None] * rows)

    for (x, y), item in enumerate_n(matrix, n=2):
        transposed_matrix[y][x] = item

    return transposed_matrix


with open('input.txt') as f:
    matrix = [re.sub(r'\s+', ' ', l.strip()).split(' ') for l in f.readlines()]


matrix = transpose_matrix(matrix)
total = 0
operators = {
    '*': operator.mul,
    '+': operator.add
}

for l in matrix:
    operator = operators[l[-1]]
    total += reduce(operator, (int(i) for i in l[:-1]))

print(total)
