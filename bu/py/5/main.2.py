from itertools import *
from more_itertools import *
from fileinput import input

maps = ''.join(input()).split('\n\n')

seeds = maps[0]
maps = maps[1:]

seeds = list(map(int, seeds.split()[1:]))

seed_ranges = sorted(list(chunked(seeds, 2)), key=lambda p: p[0])
print(f'seed ranges: {seed_ranges}')

maps = list(map(
    lambda mp: list(map(lambda l: list(map(int, l.split())), mp.strip().split('\n')[1:])),
    maps
))

for loc in range(107000000, 200000000):
    if loc % 1000000 == 0: print(loc)
    seed = loc
    for mp in maps[::-1]:
        if m := next((m for m in mp if m[0] <= seed and seed <= m[0] + m[2]), None):
            seed -= m[0] - m[1]
    for beg, ln in seed_ranges:
        if beg <= seed and seed <= (beg+ln):
            print(f'answer: {loc}')
            exit(0)
