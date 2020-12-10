from pathlib import PosixPath
from typing import Dict, Set

in_data = list(map(int, (PosixPath(".") / "day9.txt").read_text().split()))


def setup(preamble_length, data):
    included_in: Dict[int, Dict[int, int]] = {}
    sums: Dict[int, int] = {}

    for num in data[:preamble_length]:
        included_in[num] = {}

    for i in range(preamble_length - 1):
        addend1 = data[i]
        for j in range(i+1, preamble_length):
            addend2 = data[j]
            result = addend1 + addend2
            included_in[addend1][addend2] = result
            included_in[addend2][addend1] = result
            if result in sums:
                sums[result] += 1
            else:
                sums[result] = 1

    return sums, included_in


def remove_number(number: int, sums: Dict[int, int], included_in: Dict[int, Dict[int, int]]):
    new_included_in = {}
    for addend, result in included_in.items():
        if addend == number:
            continue
        if addend in included_in[number]:
            result.pop(number)
        new_included_in[addend] = result

    for result in included_in[number].values():
        if sums[result] == 1:
            del sums[result]
        else:
            sums[result] -= 1

    return new_included_in


def add_number(number: int, sums: Dict[int, int], included_in: Dict[int, Dict[int, int]]):
    included_in[number] = {}
    for addend in included_in:
        result = number + addend
        included_in[number][addend] = result
        included_in[addend][number] = result
        if result in sums:
            sums[result] += 1
        else:
            sums[result] = 1


preamble_length = 25
sums, included_in = setup(preamble_length, in_data)
preamble = in_data[:preamble_length]
goal = 0
goal_index = 0


for i in range(preamble_length, len(in_data)):
    number = in_data[i]
    if number not in sums:
        goal = number
        goal_index = i
        break
    else:
        included_in = remove_number(preamble[0], sums, included_in)
        add_number(number, sums, included_in)
        preamble.pop(0)
        preamble.append(number)


def find_encryption_weakness(goal, goal_index):
    for j in range(len(in_data[:goal_index])):
        curr_number = in_data[j]
        curr_sum = curr_number
        numbers = [curr_number]
        for addend in in_data[j+1:goal_index]:
            curr_sum += addend
            numbers.append(addend)
            if curr_sum == goal:
                return min(numbers) + max(numbers)
    
            if curr_sum > goal:
                break


print(find_encryption_weakness(goal, goal_index))

