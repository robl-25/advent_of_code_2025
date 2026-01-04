from dataclasses import dataclass
from dataclasses import field


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


@dataclass
class Node:
    symbol: str
    coords: tuple
    matrix: list=field(repr=False)

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

    # All neighbors in `self.directions`.
    def neighbors(self):
        return [self._neighbor(direction) for direction in self.directions if self._neighbor(direction) is not None]

    def is_accessible(self):
        return len([n for n in self.neighbors() if n.symbol == '@']) < 4

    def remove(self):
        self.symbol = '.'


with open('input.txt') as f:
    nodes = [list(l.strip()) for l in f.readlines()]

for coords, symbol in enumerate_n(nodes, n=2):
    nodes[coords[0]][coords[1]] = Node(symbol=symbol, coords=coords, matrix=nodes)

total = 0
nodes_to_remove = [node for _, node in enumerate_n(nodes, n=2) if node.symbol == '@' and node.is_accessible()]

while nodes_to_remove:
    total += len(nodes_to_remove)

    for node in nodes_to_remove:
        node.remove()

    nodes_to_remove = [node for _, node in enumerate_n(nodes, n=2) if node.symbol == '@' and node.is_accessible()]

print(total)
