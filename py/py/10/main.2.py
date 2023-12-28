from fileinput import input
from more_itertools import *
from pprint import pprint

grid = ''.join(input()).strip().split('\n')
w, h = len(grid[0]), len(grid)
grid = ''.join(grid)

print(grid)

dists = [-1] * len(grid)

def oob(p, w, h):
    return p < 0 or p >= w*h

def neighs_r(grid, p):
    def oob(p):
        return p < 0 or p >= w*h

    # Connected north
    if not oob(p - w) and grid[p] in '|JLS' and grid[p-w] in '|7F':
        if grid[p] in 'L': r = 1
        if grid[p] in 'J': r = -1
        else: r = 0
        yield p - w, r
    # Connected south
    if not oob(p + w) and grid[p] in '|7FS' and grid[p+w] in '|JL':
        if grid[p] in '7': r = 1
        if grid[p] in 'F': r = -1
        else: r = 0
        yield p + w, r
    # Connected west
    if not oob(p - 1) and grid[p] in '-J7S' and grid[p-1] in '-LF':
        if grid[p] in 'J': r = 1
        if grid[p] in '7': r = -1
        else: r = 0
        yield p - 1, r
    # Connected east
    if not oob(p + 1) and grid[p] in '-LFS' and grid[p+1] in '-J7':
        if grid[p] in 'F': r = 1
        if grid[p] in 'L': r = -1
        else: r = 0
        yield p + 1, r

def neighs(grid, p):
    return map(lambda p: p[0], neighs_r(grid, p))

def flood(loop, vis, sp):
    print(sp//w, sp%w)
    f = flood_h(loop, vis, sp, 875 + 63 + 32 + 16 + 8 + 2)
    # pprint(list(chunked(map(int, vis), w)))
    return f

def flood_h(loop, visit, p, lim):
    if lim == 0: return 0
    if oob(p, w, h): return 0
    if visit[p] == 1: return 0
    if loop[p] != -1: return 0
    visit[p] = 1
    return 1 + flood_h(loop, visit, p + w, lim - 1) \
        + flood_h(loop, visit, p - w, lim - 1) \
        + flood_h(loop, visit, p + 1, lim - 1) \
        + flood_h(loop, visit, p - 1, lim - 1)

s = grid.find('S')
print(list(map(lambda p: (p//w,p%w), neighs(grid, s))))
s1, s2 = neighs(grid, s)
dists[s] = 0

d = 1
r1 = 0
r2 = 0
p1, p2 = s1, s2
while p1 != p2:
    dists[p1] = d
    dists[p2] = d
    if not (p := next(filter(lambda p: dists[p[0]] == -1, neighs_r(grid, p1)), None)):
        assert(False)
    p1 = p[0]
    r1 += p[1]
    if not (p := next(filter(lambda p: dists[p[0]] == -1, neighs_r(grid, p2)), None)):
        assert(False)
    p2 = p[0]
    r2 += p[1]
    d += 1
dists[p1] = d
print(f'loop found: {d}')
# print('\n'.join(map(str, chunked(dists, w))))

r1 -= r2
p = s1
f = 0
vis = [0] * len(grid)
vis[s] = 2
pv = s
while p:
    vis[p] = 2
    # if grid[p] in '|-':
    if r1 > 0:
        # print('r1>0')
        if p - pv == -w:
            f += flood(dists, vis, p + 1)
        if p - pv == w:
            f += flood(dists, vis, p - 1)
        if p - pv == -1:
            f += flood(dists, vis, p - w)
        if p - pv == 1:
            f += flood(dists, vis, p + w)
    elif r1 <= 0:
        # print('r1<0')
        if p - pv == -w:
            f += flood(dists, vis, p - 1)
        if p - pv == w:
            f += flood(dists, vis, p + 1)
        if p - pv == -1:
            f += flood(dists, vis, p + w)
        if p - pv == 1:
            f += flood(dists, vis, p - w)
    # else:
    #     assert(False)
    pv = p
    p = next(filter(lambda p: vis[p] != 2, neighs(grid, p)), None)
print(f'ans: {f}')
