from fileinput import input

maps = ''.join(input()).split('\n\n')

seeds = maps[0]
maps = maps[1:]

seeds = list(map(int, seeds.split()[1:]))
print(f'seeds: {seeds}')

maps = list(map(
    lambda mp: list(map(lambda l: list(map(int, l.split())), mp.strip().split('\n')[1:])),
    maps
))

# print(maps)

min_seed = float('inf')
for seed in seeds:
    acc = seed
    for mp in maps:
        print(f'DB: {mp}')
        found = False
        for mapping in mp:
            if mapping[1] <= acc and acc <= (mapping[1] + mapping[2]):
                # print(mapping)
                found = True
                acc = acc - (mapping[1] - mapping[0])
                # print(acc)
                break
        if not found:
            acc = acc
            # print(acc)
    min_seed = min(min_seed, acc)
print(f'min: {min_seed}')
