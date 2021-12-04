def main():
    with open("input.txt", "r") as f:
        previous = None
        count = 0
        for i in f.readlines():
            if previous and int(i) > previous:
                count += 1
            previous = int(i)
        print(count)


if __name__ == '__main__':
    main()
