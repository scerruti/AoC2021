def main(file):
    with open(file, 'r') as f:
        crabs = list(map(int,f.readline().split(',')))

    crabs.sort()
    center = int(len(crabs) / 2) - 1
    if len(crabs) % 2 == 1:
        result = crabs[center]
    else:
        result = int((int(crabs[center]) + int(crabs[center+1]))/2 + 0.5)

    print(result)
    score(result, crabs)
    score(result-1, crabs)
    score(result+1, crabs)

    average = int(sum(crabs)/len(crabs))
    print(average)
    score2(average, crabs)

    min_fuel = 94865123
    min_n = None
    for i in range(200):
        fuel = score2(average-100+i, crabs)
        if fuel < min_fuel:
            min_fuel = fuel
            min_n = average-100+i
    print(min_fuel, min_n)


def score(n, crabs):
    print(n, sum(list(map(lambda x: abs(n-x), crabs))))


def score2(n, crabs):
    fuel = 0
    for crab in crabs:
        distance = abs(n-crab)
        fuel += (distance+1) * (distance/2)
        # print(crab, distance, fuel)

    #print(n, fuel)
    return fuel


if __name__ == '__main__':
    main('input.txt')
