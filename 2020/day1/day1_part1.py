from pathlib import PosixPath

path = PosixPath(".") / "day1.txt"
data = path.read_text().split()

result = None
for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        print(f"{data[i]} + {data[j]} = {int(data[i]) + int(data[j])}")
        if int(data[i]) + int(data[j]) == 2020:
            result = int(data[i]) * int(data[j])
            break

    if result:
        break

print(result)
