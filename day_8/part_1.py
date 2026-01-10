from dataclasses import dataclass
from dataclasses import field
from pprint import pp
from itertools import combinations

import bisect
import math


@dataclass
class Node:
    coords: tuple
    nearest_node: 'Node'=field(default=None, repr=False)

    def __eq__(self, other):
        return self.coords == other.coords

    def __hash__(self):
        return hash(self.coords)


@dataclass
class Connection:
    distance: float
    node_a: 'Node'
    node_b: 'Node'


with open('input.txt') as f:
    nodes = [Node(coords=tuple(int(i) for i in l.strip().split(','))) for l in f.readlines()]

connections = []

for node_a, node_b in combinations(nodes, 2):
    connection = Connection(
        node_a=node_a,
        node_b=node_b,
        distance=math.dist(node_a.coords, node_b.coords)
    )

    bisect.insort(connections, connection, key=lambda c: c.distance)

circuits = sorted(({node} for node in nodes))

for connection in connections[:1000]:
    a, b = connection.node_a, connection.node_b
    circuit = {a, b}

    a_index, a_circuit = next((i, c) for i, c in enumerate(circuits) if a in c)
    b_index, b_circuit = next((i, c) for i, c in enumerate(circuits) if b in c)

    target_circuit = a_circuit | b_circuit

    if a_circuit == b_circuit:
        continue

    circuits.pop(max([a_index, b_index]))
    circuits.pop(min([a_index, b_index]))

    bisect.insort(circuits, target_circuit | circuit, key=lambda c: len(c))


print(len(circuits[-1]) * len(circuits[-2]) * len(circuits[-3]))
