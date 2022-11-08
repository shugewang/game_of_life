def create_new_grid(number_rows, number_cols):
    grid = []
    for row in range(number_rows):
        grid.append([])
        for col in range(number_cols):
            grid[row].append(False)
    return grid


def change_cell_status(grid, row_index, col_index, new_status):
    grid[row_index][col_index] = new_status
    return grid


def get_sum_alive_neighbours(grid, row_index, col_index):
    sum_alive_neighbour = 0
    if grid[row_index-1][col_index-1] == True and row_index >= 1 and col_index >= 1:
        sum_alive_neighbour += 1
    if grid[row_index-1][col_index] == True and row_index >= 1:
        sum_alive_neighbour += 1
    if grid[row_index-1][col_index+1] == True and row_index >= 1 and col_index < len(grid[0]):
        sum_alive_neighbour += 1
    if grid[row_index][col_index-1] == True and col_index >= 1:
        sum_alive_neighbour += 1
    if grid[row_index][col_index+1] == True and col_index < len(grid[0]):
        sum_alive_neighbour += 1
    if grid[row_index+1][col_index-1] == True and row_index < len(grid) and col_index >= 1:
        sum_alive_neighbour += 1
    if grid[row_index+1][col_index] == True and row_index < len(grid):
        sum_alive_neighbour += 1
    if grid[row_index+1][col_index+1] == True and row_index < len(grid) and col_index < len(grid[0]):
        sum_alive_neighbour += 1
    return sum_alive_neighbour


def apply_rules(grid, row_index, col_index, sum_alive_neighbour):
    current_cell_status = grid[row_index][col_index]
    if sum_alive_neighbour < 2:
        new_cell_status = False
    if current_cell_status == True and sum_alive_neighbour == 2 or sum_alive_neighbour == 3:
        new_cell_status = True
    if current_cell_status == True and sum_alive_neighbour > 3:
        new_cell_status = False
    if current_cell_status == False and sum_alive_neighbour == 3:
        new_cell_status = True

    change_cell_status(grid, row_index, col_index, new_cell_status)


# TODO: apply to all cells
# TODO: run for n generations
# TODO: randomise starting cell status

def main():
    grid = create_new_grid(3, 3)
    change_cell_status(grid, 0, 0, True)
    change_cell_status(grid, 0, 1, True)
    change_cell_status(grid, 0, 2, True)
    alive_neighbours = get_sum_alive_neighbours(grid, 1, 1)
    print(grid)
    apply_rules(grid, 1, 1, alive_neighbours)
    print(grid)
    print(alive_neighbours)


main()