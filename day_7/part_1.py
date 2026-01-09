from dataclasses import dataclass
from dataclasses import field


@dataclass
class Node:
    symbol: str
    coords: tuple
    matrix: list=field(repr=False)
    visited: bool=False

    directions = {
        'north': (-1, 0),
        'south': (1, 0),
        'west': (0, -1),
        'east': (0, 1),
        'northeast': (-1, 1),
        'northwest': (-1, -1),
        'southeast': (1, 1),
        'southwest': (1, -1)
    }

    # Gets neighbor in `self.matrix` given a `direction`.
    def _neighbor(self, direction):
        neighbor_coords = (
            self.coords[0] + self.directions[direction][0],
            self.coords[1] + self.directions[direction][1]
        )

        if neighbor_coords[0] not in range(len(self.matrix)):
            return None

        if neighbor_coords[1] not in range(len(self.matrix[0])):
            return None

        return self.matrix[neighbor_coords[0]][neighbor_coords[1]]


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


with open('input.txt') as f:
    matrix = [list(l.strip()) for l in f.readlines()]

for coords, symbol in enumerate_n(matrix, n=2):
    matrix[coords[0]][coords[1]] = Node(
        symbol=symbol,
        coords=coords,
        matrix=matrix
    )

start = next(n for n in matrix[0] if n.symbol == 'S')
splitters_hit = 0

nodes = [start]

while nodes:
    node = nodes.pop(0)

    if node.visited:
        continue

    node.visited = True
    neighbors = []

    if node.symbol == '^':
        splitters_hit += 1

        neighbors.append(node._neighbor('east'))
        neighbors.append(node._neighbor('west'))
    else:
        neighbors.append(node._neighbor('south'))

    for n in neighbors:
        if n is not None:
            nodes.append(n)


print(splitters_hit)
