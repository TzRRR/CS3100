
def max_run(grid):
    rows, cols = len(grid), len(grid[0])
    global mem
    mem = [[-1 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            helper(grid, i, j)

    max_distance = 0
    max_index = [-1, -1]
    for i in range(len(mem)):
        for j in range(len(mem[0])):
            if mem[i][j] > max_distance:
                max_distance = mem[i][j]
                max_index = (i, j)

    print(max_index[0], max_index[1])
    while max_distance > 1:
        max_distance -= 1
        if 0 <= max_index[0] - 1 < len(mem) and 0 <= max_index[1] < len(mem) and mem[max_index[0] - 1][max_index[1]] == max_distance:
            max_index = (max_index[0] - 1, max_index[1])
        elif 0 <= max_index[0] + 1 < len(mem) and 0 <= max_index[1] < len(mem) and mem[max_index[0] + 1][max_index[1]] == max_distance:
            max_index = (max_index[0] + 1, max_index[1])
        elif 0 <= max_index[0] < len(mem) and 0 <= max_index[1] - 1 < len(mem) and mem[max_index[0]][max_index[1] - 1] == max_distance:
            max_index = (max_index[0], max_index[1] - 1)
        elif 0 <= max_index[0] < len(mem) and 0 <= max_index[1] + 1 < len(mem) and mem[max_index[0]][max_index[1] + 1] == max_distance:
            max_index = (max_index[0], max_index[1] + 1)
        print(max_index[0], max_index[1])

def helper(grid, row, column):
    if mem[row][column] > -1:
        return mem[row][column]
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x, y = row + dx, column + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] < grid[row][column]:
            route = helper(grid, x, y)
            if 1 + route > mem[row][column]:
                mem[row][column] = 1 + route
    if mem[row][column] == -1:
        mem[row][column] = 1
        return 1
    else:
        return mem[row][column]
