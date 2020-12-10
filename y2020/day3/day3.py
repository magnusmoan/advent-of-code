from pathlib import PosixPath
import math

data = PosixPath("./day3.txt").read_text().split("\n")[:-1]

row_length = len(data[0])


def count_trees(stride):
    count = 0
    col = stride[0]
    for row in range(stride[1], len(data), stride[1]):
        print(f"{data[row]} - Position {col} - Item {data[row][col]}")
        if data[row][col] == "#":
            count += 1

        col = (col + stride[0]) % row_length
    return count


results = list(map(count_trees, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
print(results)
print(f"Multiplied: {math.prod(results)}")

