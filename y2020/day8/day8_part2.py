from typing import List

from y2020.day8.day8_part1 import run, in_data

acc, seen, is_done = run(in_data)
print(seen)
print(is_done)


def test_change(change_line, is_jmp, data: List[str]):
    print(f"Checking line {change_line}, which is {'jmp' if is_jmp else 'nop'}")
    if is_jmp:
        data[change_line] = data[change_line].replace("jmp", "nop")
    else:
        data[change_line] = data[change_line].replace("nop", "jmp")

    return run(data)


for i in range(len(in_data) - 1, -1, -1):
    command, number = in_data[i].split()
    if i not in seen or command == "acc":
        continue
    else:
        test_acc, test_seen, is_done = test_change(i, command == "jmp", in_data.copy())
        if is_done:
            print(f"Changed line {i} from {command}. Accumulator = {test_acc}")
            break


