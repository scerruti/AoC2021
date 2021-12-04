def main():
    with open("input.txt", "r") as f:
        depth = 0
        position = 0
        for line in f.readlines():
            command, parameter = line.split(" ")
            print(command, parameter)
            if command == 'forward':
                position += int(parameter)
            elif command == 'down':
                depth += int(parameter)
            elif command == 'up':
                depth -= int(parameter)
        print(depth*position)


if __name__ == '__main__':
    main()
