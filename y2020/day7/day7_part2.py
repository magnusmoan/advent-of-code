from pathlib import PosixPath
from typing import Dict, List

data_path = PosixPath(".") / "day7.txt"
data = data_path.read_text().split("\n")


class Node:
    def __init__(self, color):
        self.color = color
        self.children = {}

    def add_child(self, count, child):
        self.children[child] = count


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
            count = c.split()[0]
            color = " ".join(c.split()[1:])
            child = nodes[color] if color in nodes else Node(color)
            parent.add_child(int(count), child)
            nodes[color] = child

        nodes[container] = parent

    return nodes


def get_bag_count(bag: Node):
    if bag.children:
        count = 0
        for child, curr in bag.children.items():
            count += curr + curr * get_bag_count(child)
        return count
    return 0


print(get_bag_count(create_graph(data)["shiny gold"]))
