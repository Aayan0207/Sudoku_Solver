def main():
    sudoku = eval(input("Enter Sudoku:"))
    ans = solve(sudoku)
    print_answer(ans)


null = [
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
]


def solve(sudoku):
    unknowns = tosolve(sudoku)  # Recursive Backtracking Algorithm
    if len(unknowns) == 0:
        return sudoku
    for unknown in unknowns:
        move = moves(sudoku, unknown)
        for action in move:
            sudoku[unknown[0]][unknown[1]] = action
            if solve(sudoku):
                return sudoku
            sudoku[unknown[0]][unknown[1]] = 0
        return False
    return False


def solvable(sudoku):
    for i in range(9):
        for j in range(9):
            for num in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                if (
                    row(sudoku, (i, j)).count(num) > 1
                    or column(sudoku, (i, j)).count(num) > 1
                    or box(sudoku, (i, j)).count(num) > 1
                ):
                    return False
    return True


def moves(sudoku, cell):
    return list(
        {1, 2, 3, 4, 5, 6, 7, 8, 9}
        - (set(column(sudoku, cell) + row(sudoku, cell) + box(sudoku, cell)))
    )


def tosolve(sudoku):
    unknowns = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 or sudoku[i][j] == None:
                unknowns.append((i, j))
    return unknowns


def row(sudoku, cell):
    return sudoku[cell[0]]


def column(sudoku, cell):
    grids = []
    for grid in sudoku:
        grids.append(grid[cell[1]])
    return grids


def box(sudoku, cell):
    box = []
    grid1 = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    grid2 = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
    grid3 = [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]
    grid4 = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    grid5 = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
    grid6 = [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]
    grid7 = [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
    grid8 = [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)]
    grid9 = [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    grids = [grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9]
    for grid in grids:
        if cell in grid:
            for cells in grid:
                box.append(sudoku[cells[0]][cells[1]])
    return box


def print_answer(sudoku):
    for grid in sudoku:
        string = ""
        for cell in grid:
            string += str(cell) + " "
        print(string)


if __name__ == "__main__":
    main()
