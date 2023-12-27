from itertools import *
from more_itertools import *
from fileinput import input

maps = ''.join(input()).split('\n\n')

seeds = maps[0]
maps = maps[1:]

seeds = list(map(int, seeds.split()[1:]))
seed_ranges = sorted(list(chunked(seeds, 2)), key=lambda p: p[0])

maps = list(map(
    lambda mp: list(map(
        lambda l: list(map(int, l.split())),
        mp.strip().split('\n')[1:]
    )),
    maps
))


for loc in range(108956227 - 10, 200000000):
    if loc % 1000000 == 0: print(loc)
    seed = loc
    for mp in maps[::-1]:
        for mapping in mp:
            if mapping[0] <= seed and seed <= (mapping[0] + mapping[2]):
                seed = seed - (mapping[0] - mapping[1])
    for beg, ln in seed_ranges:
        if beg <= seed and seed <= (beg+ln):
            print(f'answer: {loc}')
            exit(0)
