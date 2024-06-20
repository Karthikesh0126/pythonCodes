import numpy as np
from dokusan import generators

# Generate a Sudoku puzzle using dokusan
puzzle = generators.random_sudoku(avg_rank=150)
grid = [[int(str(puzzle)[i * 9 + j]) for j in range(9)] for i in range(9)]

# Function to print the grid
def print_grid(grid):
    print(np.matrix(grid))

# Print the initial grid
print("Initial grid:")
print_grid(grid)

# Function to check if a number can be placed at the given position
def possible(row, column, number):
    global grid
    for i in range(0,9):
        if grid[row][i] == number:
            return False
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == number:
                return False
    return True

# Function to solve the Sudoku
def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
    print("Solved grid:")
    print_grid(grid)
    input('Press enter to exit')

# Solve the Sudoku
solve()