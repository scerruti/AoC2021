from math import prod

def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    grid = [[int(c) for c in line.strip()] for line in lines]

    low_points = []
    low_grid = []
    for i in range(len(lines)):
        low_grid.append([0]*len(lines[0]))
    for row, line in enumerate(lines):
        for col, cell in enumerate(line.strip()):
            if int(cell) < min(neighbors(row, col, grid)):
                low_points.append(int(cell))
            if int(cell) != 9:
                low_grid[row][col] = 1


    print(low_points)
    print(sum([point+1 for point in low_points]))
    for r in range(len(low_grid)):
        for c in range(len(low_grid[r])):
            print(low_grid[r][c], end='')
        print()

    basin_measured = []
    for i in range(len(lines)):
        basin_measured.append([0]*len(lines[0]))
    basins = []
    for r in range(len(low_grid)):
        for c in range(len(low_grid[r])):
            if basin_measured[r][c] == 0:
                basin_size = measure_basin(r, c, low_grid, basin_measured, 0)
                if basin_size > 0:
                    print(basin_size)
                    basins.append(basin_size)
    basins.sort()
    print(prod(basins[-3:]))


def measure_basin(r, c, low_grid, basin_measured, depth):
    depth += 1
    if r < 0 or c < 0 or r > len(low_grid)-1 or c > len(low_grid[r]) - 1 or low_grid[r][c] == 0 or basin_measured[r][c] == 1:
        return  0
    print('->', r, c, len(low_grid)-1, len(low_grid) - 1, low_grid[r][c], depth)

    basin_measured[r][c] = 1
    result = 1
    result += measure_basin(r-1, c, low_grid, basin_measured, depth)
    result += measure_basin(r+1, c, low_grid, basin_measured, depth)
    result += measure_basin(r, c-1, low_grid, basin_measured, depth)
    result += measure_basin(r, c+1, low_grid, basin_measured, depth)
    return result


def neighbors(r, c, grid):
    result = []
    if r > 0:
        result.append(grid[r-1][c])
    if r < len(grid)-1:
        result.append(grid[r+1][c])
    if c > 0:
        result.append(grid[r][c-1])
    if c < len(grid[r])-1:
        result.append(grid[r][c+1])

    return result


if __name__ == '__main__':
    main('input.txt')
