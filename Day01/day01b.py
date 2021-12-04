def main():
    with open("input.txt", "r") as f:
        count = 0
        list_of_numbers = []
        for index, value in enumerate(f.readlines()):
            list_of_numbers.append(int(value))
            if index >= 3 and sum(list_of_numbers[index - 2: index+1]) > sum(list_of_numbers[index - 3: index]):
                count += 1
        print(count)


def algorithm_2():
    with open("input.txt", "r") as f:
        value1 = None
        value2 = None
        value3 = None
        count = 0
        for index, value in enumerate(f.readlines()):
            value4 = int(value)
            if value1 and sum([value4, value3, value2]) > sum([value3, value2, value1]):
                count += 1
            value1 = value2
            value2 = value3
            value3 = value4
        print(count)

if __name__ == '__main__':
    algorithm_2()
