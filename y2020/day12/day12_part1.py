from pathlib import PosixPath
from typing import List

in_data = (PosixPath(".") / "day12.txt").read_text().split("\n")


def execute(instructions: List[str]):
    north = 0
    east = 0
    direction = 0
    degree_to_direction = {0: "E", 90: "N", 180: "W", 270: "S", -90: "S", -180: "W", -270: "N"}
    for instruction in instructions:
        letter = instruction[0]
        number = int(instruction[1:])
        if letter == "F":
            letter = degree_to_direction[direction]
        if letter == "N":
            north += number
        elif letter == "S":
            north -= number
        elif letter == "W":
            east -= number
        elif letter == "E":
            east += number
        elif letter == "L":
            print(f"Before {direction}, change {number}")
            direction = (direction + number) % 360
            print(f"After {direction}")
        elif letter == "R":
            print(f"Before {direction}, change {number}")
            direction = (direction - number) % 360
            print(f"After {direction}")

    return abs(north) + abs(east)


print(execute(in_data))
