def most_frequent(list, place):
    result = 0
    for item in list:
        if item[place] == "1":
            result += 1
        else:
            result -= 1
    if result >= 0:
        return 1
    else:
        return 0


def least_frequent(list, place):
    result = 0
    for item in list:
        if item[place] == "1":
            result += 1
        else:
            result -= 1
    if result >= 0:
        return 0
    else:
        return 1


def main():
    with open("input.txt", "r") as f:
        readings = f.readlines()

        oxygen = readings
        co2 = readings

        for i in range(len(readings[0])):
            if len(oxygen) > 1:
                candidate = most_frequent(oxygen, i)
                oxygen = list(filter(lambda reading: reading[i] == str(candidate), oxygen))
        print()

        for i in range(len(readings[0])):
            if len(co2) > 1:
                candidate = least_frequent(co2, i)
                co2 = list(filter(lambda reading: reading[i] == str(candidate), co2))
        print(int(oxygen[0].strip(),2)*int(co2[0].strip(), 2))


if __name__ == '__main__':
    main()
