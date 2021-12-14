def main(file):
    points = []

    with open(file, 'r') as f:
        lines = f.readlines()
    index = 0
    line = lines[index]
    while line.strip():
        (x,y) = map(int,line.strip().split(','))
        points.append((x, y))
        index += 1
        line = lines[index]

    index += 1
    while index < len(lines):
        parts = lines[index].strip().split(' ')
        fold_dir, fold_line = parts[2].split('=')
        fold_line = int(fold_line)

        if fold_dir == 'x':
            points = set([(x if x < fold_line else fold_line - (x - fold_line), y) for (x,y) in points])
        else:
            points = set([(x, y if y < fold_line else fold_line - (y - fold_line)) for (x,y) in points])
        index += 1
        print(len(points))
        print(fold_dir, fold_line)
        print(min([x for (x,y) in points]), max([x for (x,y) in points])+1, min([y for (x,y) in points]), max([y for (x, y) in points])+1)

    print(len(points))
    print_points(points)


def print_points(points ):
    x_min = min([x for (x,y) in points])
    x_max = max([x for (x,y) in points])+1
    y_min = min([y for (x,y) in points])
    y_max = max([y for (x, y) in points])+1

    code = [['.']*(x_max - x_min) for _ in range(y_max - y_min)]
    for (x, y) in points:
        code[y-y_min][x-x_min] = '#'

    for code_line in code:
        print(''.join(code_line))


if __name__ == '__main__':
    main('input.txt')
