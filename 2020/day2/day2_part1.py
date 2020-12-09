from pathlib import PosixPath

path = PosixPath(".") / "day2.txt"

data = path.read_text().split("\n")[:-1]


def is_valid(line: str) -> bool:
    policy = line.split(":")[0]
    min_occ = int(policy.split("-")[0])
    max_occ = int(policy.split("-")[1].split()[0])
    letter = policy.split("-")[1].split()[1]

    password = line.split(":")[1]
    count = password.count(letter)

    return min_occ <= count <= max_occ


print(len(list(filter(is_valid, data))))

