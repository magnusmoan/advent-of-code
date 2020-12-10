from pathlib import PosixPath

in_data = list(map(int, (PosixPath(".") / "day10.txt").read_text().split()))

sorted_data = sorted(in_data)

jolt_3 = 1
jolt_1 = 0

for i in range(len(sorted_data)-1):
    curr = sorted_data[i]
    next = sorted_data[i+1]
    if next - curr == 1:
        jolt_1 += 1
    elif next - curr == 3:
        jolt_3 += 1

if sorted_data[0] == 1:
    jolt_1 += 1
elif sorted_data[0] == 3:
    jolt_3 += 1

print(jolt_1 * jolt_3)
