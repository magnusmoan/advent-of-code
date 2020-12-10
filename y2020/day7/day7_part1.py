from pathlib import PosixPath
from typing import Dict, List

data_path = PosixPath(".") / "day7.txt"
data = data_path.read_text().split("\n")


class Node:
    def __init__(self, color):
        self.color = color
        self.parents = []

    def add_parent(self, parent):
        self.parents.append(parent)


def create_graph(data):
    nodes: Dict[str, Node] = {}

    for line in data:
        cleaned = line.replace("bags", "").replace("bag", "").replace(".", "").split("contain")
        container = cleaned[0].strip()
        contained = list(map(str.strip, cleaned[1].split(",")))

        parent = nodes[container] if container in nodes else Node(container)
        if contained[0] == "no other":
            continue

        for c in contained:
            color = " ".join(c.split()[1:])
            child = nodes[color] if color in nodes else Node(color)
            child.add_parent(parent)
            nodes[color] = child

        nodes[container] = parent

    return nodes


nodes = create_graph(data)
parents: List[List[Node]] = [nodes["shiny gold"].parents]
possible = set()

while parents:
    current = parents.pop()
    for parent in current:
        if parent.color in possible:
            continue
        possible.add(parent.color)
        parents.append(parent.parents)

print(len(set(possible)))

