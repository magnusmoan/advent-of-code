from pathlib import PosixPath

data_path = PosixPath(".") / "day6.txt"
data = data_path.read_text().split("\n\n")

count = 0
for d in data:
    d = d.replace("\n", "")
    count += len(set(d))

print(count)
