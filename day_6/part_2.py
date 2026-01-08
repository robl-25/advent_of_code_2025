
import re
import operator

from pprint import pp
from functools import reduce
from itertools import zip_longest


def to_numbers(l):
    return [tuple_to_number(t) for t in zip_longest(*l)]


def tuple_to_number(t):
    return int(''.join(i for i in t if i is not None))


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


operators = {
    '*': operator.mul,
    '+': operator.add
}

with open('input.txt') as f:
    matrix = [list(l.strip('\n')) for l in f.readlines()]

    splitting_indexes = [y - 1 for (_, y), symbol in enumerate_n(matrix, n=2) if symbol in operators and y > 0]

    for (x, y), _ in enumerate_n(matrix, n=2):
        if y in splitting_indexes:
            matrix[x][y] = ','

    matrix = [''.join(l).split(',') for l in matrix]

matrix = transpose_matrix(matrix)
total = 0

for l in matrix:
    operator = operators[l[-1].strip()]
    nums = to_numbers(l[:-1])

    total += reduce(operator, to_numbers(l[:-1]))

print(total)
