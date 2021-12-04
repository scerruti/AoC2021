def main():
    with open("input.txt", "r") as f:
        depth = 0
        position = 0
        aim = 0
        for line in f.readlines():
            command, parameter = line.split(" ")
            if command == 'forward':
                position += int(parameter)
                depth += int(parameter) * aim
            elif command == 'down':
                aim += int(parameter)
            elif command == 'up':
                aim -= int(parameter)
        print(depth*position)


if __name__ == '__main__':
    main()
