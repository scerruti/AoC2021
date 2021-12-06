import re


def add_line(vent_map, points):
    x1  = int(points[0][0])
    y1  = int(points[0][1])
    x2  = int(points[1][0])
    y2  = int(points[1][1])
    rise = (y2 - y1)
    run = (x2 - x1)

    # Part 1: Uncomment to ignore diagonals
    # if rise != 0 and run != 0:
    #     return

    x_step = 1 if run > 0 else -1 if run < 0 else 0
    y_step = 1 if rise > 0 else -1 if rise < 0 else 0

    num_points = max(abs(rise), abs(run)) + 1
    x = x1
    y = y1
    for _ in range(num_points):
        vent_map[(x, y)] = vent_map[(x, y)] + 1 if (x, y) in vent_map else 1
        x += x_step
        y += y_step


def add_line_from_regex(vent_map, result):
    x1 = int(result.group(1))
    y1 = int(result.group(2))
    x2 = int(result.group(3))
    y2 = int(result.group(4))
    add_line(vent_map, [[x1, y1], [x2, y2]])


def read_lines(file_name):
    vent_map = {}
    # program = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    # with open(file_name, "r") as f:
    #     for line in f.readlines():
    #         result = program.match(line)
    #         add_line(vent_map, result)
    with open(file_name, "r") as f:
        for line in f.readlines():
            points = [p.split(',') for p in line.split(' -> ')]
            add_line(vent_map, points)
    return vent_map


def part1(vent_map):
    print(len([vent for vent in vent_map.values() if vent > 1]))


def print_map(vent_map):
    locations = vent_map.keys()
    min_row = min([location[1] for location in locations])
    max_row = max([location[1] for location in locations])
    min_col = min([location[0] for location in locations])
    max_col = max([location[0] for location in locations])

    for y in range(min_row, max_row+1):
        for x in range(min_col, max_col + 1):
            print(vent_map[(x, y)] if (x, y) in vent_map else '.', end='')
        print()


if __name__ == '__main__':
    vents = read_lines('test_input.txt')
    print_map(vents)
    part1(vents)
