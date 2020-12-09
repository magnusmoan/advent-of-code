from pathlib import PosixPath

data_path = PosixPath(".") / "day6.txt"
data = data_path.read_text().split("\n\n")

count = 0
for d in data:
    d = d.split("\n")
    sets = []
    for person in d:
        sets.append(set(person))

    if len(sets) == 1:
        count += len(sets[0])
    else:
        count += len(sets[0].intersection(*sets[1:]))

print(count)
