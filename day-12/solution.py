from enum import Enum
from collections import Counter


class NodeType(Enum):
    SMALL = 1
    LARGE = 2
    START = 3
    END = 4


class Node:
    def __init__(self, name):
        self.type = Node._get_node_type(name)
        self.name = name
        self._neighbors = []

    def add_neighbor(self, node):
        if node not in self._neighbors:
            self._neighbors.append(node)

    def get_neighbors(self):
        return self._neighbors

    def get_available_neighbors(self, path, ruleset_version):

        # Part 1 rules allow for visiting small nodes only once
        if ruleset_version == "Part 1 Rules":
            return [node for node in self._neighbors if not (node.type == NodeType.SMALL and node in path) and node.type != NodeType.START]

        # Part 1 rules allow for visiting one small node twice in a journey
        if ruleset_version == "Part 2 Rules":

            # TODO: Needs some cleanup since this generates a couple extra iterations we throw away to ge the right result
            c = Counter()
            for node in path:
                if node.type == NodeType.SMALL:
                    c[node.name] += 1
            max_small_cave = 0
            if len(c) > 0:
                max_small_cave = len([i for i in c.values() if i >= 2])

            if max_small_cave == 1:
                return [node for node in self._neighbors if not (node.type == NodeType.SMALL and node in path) and node.type != NodeType.START]
            if max_small_cave > 1:
                return []
            else:
                return [node for node in self._neighbors if node.type != NodeType.START]

    @staticmethod
    def _get_node_type(name):
        if name == 'start':
            return NodeType.START
        elif name == 'end':
            return NodeType.END
        elif name == name.lower():
            return NodeType.SMALL
        elif name == name.upper():
            return NodeType.LARGE
        else:
            raise ValueError

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


def traverse(node, ruleset_version, path=()):
    path = path + (node,)
    if node.type == NodeType.END:
        return 1
    elif len(node.get_available_neighbors(path, ruleset_version)) == 0:
        return 0
    else:
        return 0 + sum((
                traverse(i, ruleset_version, path) for i in node.get_available_neighbors(path, ruleset_version)
            ))


if __name__ == "__main__":
    data = []
    with open("input.txt") as infile:
        for line in infile:
            data.append(line.strip().split("-"))
    nodes = {}
    for node_1, node_2 in data:
        if node_1 not in nodes.keys():
            nodes[node_1] = Node(node_1)
        if node_2 not in nodes.keys():
            nodes[node_2] = Node(node_2)
        nodes[node_1].add_neighbor(nodes[node_2])
        nodes[node_2].add_neighbor(nodes[node_1])

    print(traverse(nodes['start'], "Part 1 Rules"))
    print(traverse(nodes['start'], "Part 2 Rules"))
