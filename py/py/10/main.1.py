from fileinput import input
from more_itertools import *
from pprint import pprint

grid = ''.join(input()).strip().split('\n')
w, h = len(grid[0]), len(grid)
grid = ''.join(grid)

print(grid)

dists = [-1] * len(grid)

def neighs(grid, p):
    def oob(p):
        return p < 0 or p >= w*h

    # Connected north
    if not oob(p - w) and grid[p] in '|JLS' and grid[p-w] in '|7F':
        yield p - w
    # Connected south
    if not oob(p + w) and grid[p] in '|7FS' and grid[p+w] in '|JL':
        yield p + w
    # Connected west
    if not oob(p - 1) and grid[p] in '-J7S' and grid[p-1] in '-LF':
        yield p - 1
    # Connected east
    if not oob(p + 1) and grid[p] in '-LFS' and grid[p+1] in '-J7':
        yield p + 1

p = grid.find('S')
print(list(map(lambda p: (p//w,p%w), neighs(grid, p))))
p1, p2 = neighs(grid, p)
dists[p] = 0

d = 1
while p1 != p2:
    dists[p1] = d
    dists[p2] = d
    if not (p1 := next(filter(lambda n: dists[n] == -1, neighs(grid, p1)), None)):
        assert(False)
    if not (p2 := next(filter(lambda n: dists[n] == -1, neighs(grid, p2)), None)):
        assert(False)
    d += 1
print('\n'.join(map(str, chunked(dists, w))))
print(f'answer: {d}')
