def main():
    with open("input.txt", "r") as f:
        gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
        for line in f.readlines():
            for position in range(len(line.strip())):
                gamma[position] += 1 if line[position] == str(1) else -1
        gamma_factor = 0
        epsilon_factor = 0
        for place, bit in enumerate(gamma):
            print(bit, place)
            gamma_factor += pow(2, 11 - place) if int(bit) > 0 else 0
            epsilon_factor += pow(2, 11 - place) if int(bit) < 0 else 0

        print(gamma_factor * epsilon_factor)


if __name__ == '__main__':
    main()
