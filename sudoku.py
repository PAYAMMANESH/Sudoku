import time

def solveSudoku(grid, row, col):
    if (row == 9 - 1 and col == 9):
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, 9 + 1, 1):

        if isSafe(grid, row, col, num):
            grid[row][col] = num
            if solveSudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


def isSafe(sudoku, row, col, number):
    if (is_num_valid_in_row(sudoku, row, number)
            and is_num_valid_in_col(sudoku, col, number)
            and is_num_valid_in_square(sudoku, 3 * (row // 3), 3 * (col // 3), number)):

        return True
    else:
        return False


def is_num_valid_in_row(sudoku, row, number):
    for j in range(9):
        if sudoku[row][j] == number:
            return False
    return True


def is_num_valid_in_col(sudoku, col, number):
    for i in range(9):
        if sudoku[i][col] == number:
            return False
    return True


def is_num_valid_in_square(sudoku, row, col, number):
    for i in range(3):
        for j in range(3):
            if sudoku[i + row][j + col] == number:
                return False
    return True


def main():
    with open("Input.txt") as file:
        sudoku = [["" for i in range(9)] for j in range(9)]
        lines = file.readlines()
        for i in range(9):
            line = lines[i].replace(" ", "")
            for j in range(9):
                sudoku[i][j] = int(line[j])
        StartTime = time.perf_counter()
        solveSudoku(sudoku, 0, 0)
        RunTime = time.perf_counter() - StartTime

        with open("Output.txt", 'w') as f:
            for i in range(len(sudoku)):
                for j in range(9):
                    f.write(str(sudoku[i][j]))
                    f.write(" ")
                f.write("\n")
            f.write("RunTime is: ")
            f.write(str(RunTime))


if __name__ == '__main__':
    main()
