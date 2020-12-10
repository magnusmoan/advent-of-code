from pathlib import PosixPath

path = PosixPath(".") / "day1.txt"
data = path.read_text().split()

result = None
for i in range(len(data)-2):
    for j in range(i+1, len(data)-1):
        for k in range(j+1, len(data)):
            print(f"{data[i]} + {data[j]} + {data[k]} = {int(data[i]) + int(data[j]) + int(data[k])}")
            if int(data[i]) + int(data[j]) + int(data[k]) == 2020:
                result = int(data[i]) * int(data[j]) * int(data[k])
                break

        if result:
            break
    if result:
        break

print(result)
