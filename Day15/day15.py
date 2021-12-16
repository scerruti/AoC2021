import collections
import re


def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    cave = [[int(risk) for risk in line.strip()] for line in lines]
    cave_width = len(cave[0])
    cave_length = len(cave)

    (path, total_risk) = find_path(cave, 0, 0, cave_width, cave_length, [], 0, None)
    print(total_risk)


def find_path(cave, from_x, from_y, to_x, to_y, path, current_risk, lowest_risk):
    print((from_x, from_y))
    current_risk += cave[from_y][from_x]
    if lowest_risk and current_risk >= lowest_risk:
        return None
    path.append((from_x, from_y))
    if from_x == to_x and from_y == to_y:
        return path, current_risk

    neighbors = [(from_x + 1, from_y), (from_x, from_y + 1), (from_x, from_y - 1), (from_x - 1, from_y)]
    neighbors = list(filter(lambda point: 0 <= point[0] < to_x and 0 <= point[1] < to_y, neighbors))
    neighbors = list(filter(lambda point: point not in path, neighbors))

    print(neighbors)
    if len(neighbors) == 0:
        return None

    choices = [(cave[p[1]][p[0]], p[0], p[1]) for p in neighbors]
    # choices.sort()

    result_risk = None
    result_path = None
    for choice in choices:
        result = find_path(cave, choice[1], choice[2], to_x, to_y, path, current_risk, lowest_risk)
        if result:
            if not result_path or result[1] < result_risk:
                result_path = result[0]
                result_risk = result[1]

    if result_path:
        print((from_x, from_y), result_risk)
        return result_path, result_risk
    else:
        return None


if __name__ == '__main__':
    main('test_input.txt')
