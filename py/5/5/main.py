from fileinput import input

maps = ''.join(input()).split('\n\n')

seeds = maps[0]
maps = maps[1:]

seeds = list(map(int, seeds.split()[1:]))
print(seeds)

# TEST

test_seed = seeds[0]

# soil_map = list(map(lambda l: list(map(int, l.split())), maps[0].split('\n')[1:]))

maps = list(map(
    lambda m: list(map(lambda l: list(map(int, l.split())), m.split('\n')[1:])),
    maps
))

# print(maps)

found = False
for mapping in maps[0]:
    if mapping[1] <= test_seed and test_seed <= (mapping[1] + mapping[2]):
        print(mapping)
        test_soil = test_seed - (mapping[1] - mapping[0])
        print(test_soil)
        found = True
        break
if not found:
    test_soil = test_seed
    print(test_soil)

found = False
for mapping in maps[1]:
    if mapping[1] <= test_soil and test_soil <= (mapping[1] + mapping[2]):
        print(mapping)
        test_fertilizer = test_soil - (mapping[1] - mapping[0])
        print(test_fertilizer)
        break
if not found:
    test_fertilizer = test_soil
    print(test_fertilizer)
