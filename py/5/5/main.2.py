from itertools import *
from more_itertools import *
from fileinput import input

# TODO: Test this
def reverse_map(loc):
    acc = loc
    for mp in maps[::-1]:
        found = False
        for mapping in mp:
            if mapping[0] <= acc and acc <= (mapping[0] + mapping[2]):
                # print(mapping)
                found = True
                acc = acc - (mapping[0] - mapping[1])
                # print(acc)
                break
        if not found:
            acc = acc
            # print(acc)
    return acc

maps = ''.join(input()).split('\n\n')

seeds = maps[0]
maps = maps[1:]

seeds = list(map(int, seeds.split()[1:]))
# print(f'seeds: {seeds}')

seed_ranges = sorted(list(chunked(seeds, 2)), key=lambda p: p[0])
print(f'seed ranges: {seed_ranges}')

maps = list(map(
    lambda mp: list(map(lambda l: list(map(int, l.split())), mp.strip().split('\n')[1:])),
    maps
))
# print(maps)

# REVERSE MAP TEST
# print(reverse_map(82))
# print(reverse_map(43))
# print(reverse_map(86))
# print(reverse_map(35))

for loc in count():
    if loc % 1000000 == 0: print(loc)
    candidate_seed = reverse_map(loc)
    for beg, ln in seed_ranges:
        if beg <= candidate_seed and candidate_seed <= (beg+ln):
            print(f'answer: {loc}')
            exit(1)
