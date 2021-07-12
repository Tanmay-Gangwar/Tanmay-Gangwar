def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = " ")
            if j == 2 or j == 5: print("|", end = " ")
        print("")
        if i == 2 or i == 5: print("---------------------")
    print("")


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def is_valid(num, pos, grid):
    row, col = pos
    for i in range(9):
        if grid[i][col] == num: return False
        if grid[row][i] == num: return False
    Row = row // 3
    Col = col // 3
    for i in range(3):
        for j in range(3):
            if grid[3 * Row + i][3 * Col + j] == num: return False
    return True


def solve(grid):
    empty_pos = find_empty(grid)
    if empty_pos is None: return True
    row, col = empty_pos
    for num in range(1, 10):
        if is_valid(num, empty_pos, grid):
            grid[row][col] = num
            if solve(grid): return True
            grid[row][col] = 0
    return False


def main():
    print("Enter the sudoku as 9 by 9 matrix with numbers 0-9 where 0 represents a empty square: ")
    try:
        grid = [[int (x) for x in input().strip().split(" ")] for _ in range(9)]
        for row in grid:
            for num in row:
                if num < 0 or num > 9:
                    print("Numbers of Sudoku must be between 0-9.")
                    raise Exception
                    
    except Exception as e:
        print("Please enter a valid Sudoku")
        return

    print("\nUnsolved Sudoku: ")
    print_grid(grid)

    solve(grid)
    print("\n Solved Sudoku: ")
    print_grid(grid)


if __name__ == "__main__":
    main()
