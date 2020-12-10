from pathlib import PosixPath

data_path = PosixPath(".") / "day8.txt"
in_data = data_path.read_text().split("\n")


def run(data, line=0, acc=0):
    seen = {line: acc}

    while True:
        command, number = data[line].split()
        if command == "acc":
            acc += int(number)
            line += 1
        elif command == "jmp":
            line += int(number)
        elif command == "nop":
            line += 1

        if line in seen or line == len(data):
            return acc, seen, line == len(data)

        seen[line] = acc

