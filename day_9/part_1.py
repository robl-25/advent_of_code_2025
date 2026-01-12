from dataclasses import dataclass
from dataclasses import field
from pprint import pp
from itertools import combinations

import math


@dataclass
class Node:
    coords: tuple

    def __eq__(self, other):
        return self.coords == other.coords

    def __hash__(self):
        return hash(self.coords)


@dataclass
class Rectangle:
    node_a: 'Node'
    node_b: 'Node'
    area: int=0

    def __post_init__(self):
        prod = []

        for a, b in zip(self.node_a.coords, self.node_b.coords):
            if a == b:
                prod.append(1)
            else:
                prod.append(abs(b - a) + 1)

        self.area = math.prod(prod)


with open('input.txt') as f:
    nodes = []

    for l in f.readlines():
        coords = tuple(int(a) for a in l.strip().split(','))
        nodes.append(Node(coords=coords))


rectangles = []

for node_a, node_b in combinations(nodes, 2):
    rectangles.append(Rectangle(node_a=node_a, node_b=node_b))

print(max(r.area for r in rectangles))
