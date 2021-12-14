import math
from math import prod

def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    octopi = [int(octopus) for line in lines for octopus in line.strip()]

    dump(octopi)
    total_flashes = 0
    flashes = 0
    i = 0
    while flashes != len(octopi):
        i += 1
        print('Step:', i)
        octopi, flashes = step(octopi)
        # dump(octopi)
        total_flashes += flashes

    print(total_flashes)



def step(octopi):
    flashes = 0
    octopi = [(octopus + 1) % 10 for octopus in octopi]

    flashed = [octopus == 0 for octopus in octopi]
    while sum(flashed):
        flashes += sum(flashed)
        next_flashed = [False]*len(octopi)
        for index in range(len(octopi)):
            if octopi[index] != 0:
                additional_energy = flashed_neighbors(index, flashed)
                octopi[index] = (octopi[index] + additional_energy)
                if octopi[index] > 9:
                    octopi[index] = 0
                    next_flashed[index] = True
        flashed = next_flashed
    return octopi, flashes


def flashed_neighbors(index, flashed):
    side = int(math.sqrt(len(flashed)))
    row = int(index / side)
    col = index % side

    new_side = side + 2

    field = [False] * new_side
    for i in range(side):
        field.append(False)
        field.extend(flashed[i*side: (i+1)*side])
        field.append(False)
    field.extend([False] * new_side)

    new_index = index + new_side + row*2 +  1

    neighbors = [-new_side -1, -new_side, -new_side+1,
                 -1, +1,
                 +new_side - 1, +new_side, +new_side+1]
    count_of_flashed = sum([field[neighbor] for neighbor in [new_index+n for n in neighbors]])
    return count_of_flashed

def dump(octopi):
    side = int(math.sqrt(len(octopi)))
    for index, octopus in enumerate(octopi):
        print(octopus, end='')
        if index % side == side-1:
            print()
    print()



if __name__ == '__main__':
    main('input.txt')
