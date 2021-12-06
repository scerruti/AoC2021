def main(file):
    fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8:0}
    with open(file, 'r') as f:
        for fishy in f.readline().split(','):
            fish[int(fishy)] += 1

    for days in range(256):
        reproducing_fish = fish[0]
        for day in range(1, 9):
            fish[day - 1] = fish[day]
        fish[6] += reproducing_fish
        fish[8] = reproducing_fish
        print(reproducing_fish, "After", days + 1, "days:", fish)
    print(sum(fish.values()))


if __name__ == '__main__':
    main('input.txt')
