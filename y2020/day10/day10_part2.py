from pathlib import PosixPath

in_data = list(map(int, (PosixPath(".") / "day10.txt").read_text().split()))

sorted_data = sorted(in_data, reverse=True)
sorted_data.append(0)
highest = sorted_data[0]
adapter_to_comb = {highest: 1}
reachable = {highest}

for adapter in sorted_data[1:]:
    adapter_comb = 0
    unreachable = set()
    for potential in reachable:
        if potential - adapter < 4:
            adapter_comb += adapter_to_comb[potential]
            if potential - adapter == 3:
                unreachable.add(potential)
        else:
            unreachable.add(potential)

    adapter_to_comb[adapter] = adapter_comb
    reachable -= unreachable
    reachable.add(adapter)

print(adapter_to_comb[sorted_data[-1]])