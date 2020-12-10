from pathlib import PosixPath
import math


file_path = PosixPath(".") / "day5.txt"
data = file_path.read_text().split("\n")


def search_binary(row_string, upper, lower):
    for letter in row_string:
        if letter in ["F", "L"]:
            upper -= math.ceil((upper - lower) / 2)
        elif letter in ["B", "R"]:
            lower += 1 + (upper - lower) // 2

    if lower != upper:
        print(f"ERROR! {lower} != {upper} for {row_string}")
    return lower


ids = []
for d in data:
    ids.append(search_binary(d[:7], 127, 0) * 8 + search_binary(d[7:], 7, 0))

ids = sorted(ids)
prev = ids[0]
for i in ids[1:]:
    if i - prev != 1:
        print(i-1)
    prev = i
