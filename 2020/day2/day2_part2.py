from pathlib import PosixPath

path = PosixPath(".") / "day2.txt"

data = path.read_text().split("\n")[:-1]


def is_valid(line: str) -> bool:
    policy = line.split(":")[0]
    first = int(policy.split("-")[0])
    second = int(policy.split("-")[1].split()[0])
    letter = policy.split("-")[1].split()[1]

    p = line.split(":")[1]
    return (p[first] + p[second]).count(letter) == 1
     
print(len(list(filter(is_valid, data))))


