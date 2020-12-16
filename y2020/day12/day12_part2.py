from pathlib import PosixPath
from typing import List
from math import sin, cos, pi, atan

in_data = (PosixPath(".") / "day12.txt").read_text().split("\n")


def move_ship(ship, waypoint, steps):
    return ship[0] + steps * waypoint[0], ship[1] + steps * waypoint[1]


def move_by_degree(waypoint, angle_diff):
    new_angle = calc_angle(waypoint) + (angle_diff * pi / 180)
    dist = calc_distance(waypoint)
    new_x = round(dist * cos(new_angle))
    new_y = round(dist * sin(new_angle))
    return new_x, new_y


def calc_distance(waypoint):
    return (waypoint[0]**2 + waypoint[1]**2)**0.5


def calc_angle(waypoint):
    x, y = waypoint
    if y == 0:
        return -pi if x < 0 else 0
    if x == 0:
        return pi/2 if y > 0 else -pi/2

    angle = atan(y / x)
    return angle if x > 0 else angle + pi


def execute(instructions: List[str]):
    waypoint = 10, 1
    ship = 0, 0
    for instruction in instructions:
        letter = instruction[0]
        number = int(instruction[1:])
        print(f"Before: {ship} - {waypoint}")
        if letter == "F":
            ship = move_ship(ship, waypoint, number)
        if letter == "N":
            waypoint = waypoint[0], waypoint[1] + number
        elif letter == "S":
            waypoint = waypoint[0], waypoint[1] - number
        elif letter == "W":
            waypoint = waypoint[0] - number, waypoint[1]
        elif letter == "E":
            waypoint = waypoint[0] + number, waypoint[1]
        elif letter == "L":
            waypoint = move_by_degree(waypoint, number)
        elif letter == "R":
            waypoint = move_by_degree(waypoint, -number)
        print(f"After: {ship} - {waypoint}\n")
    return abs(ship[0]) + abs(ship[1])


print(execute(in_data))
