from pathlib import PosixPath

data = (PosixPath(".") / "day11.txt").read_text().split("\n")

data = [list(row) for row in data]


def add_border(board):
    for i, row in enumerate(board):
        board[i] = ["."] + row + ["."]

    top_bottom_border = ["." for _ in range(len(board[0]))]
    board.insert(0, top_bottom_border)
    board.append(top_bottom_border)


def print_board(board):
    print()
    for row in board:
        print("".join(row))


def perform_round(board, rows, cols, visible):
    new_board = [["." for _ in range(cols+2)] for _ in range(rows+2)]
    changed = False
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            seat = board[row][col]
            if seat == "#" and count_occupied_adjacent(board, row, col, visible) >= 5:
                changed = True
                new_board[row][col] = "L"
            elif seat == "L" and count_occupied_adjacent(board, row, col, visible) == 0:
                changed = True
                new_board[row][col] = "#"
            else:
                new_board[row][col] = seat

    return new_board, changed


def count_occupied_adjacent(board, row, col, visible=False):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if not visible:
                if board[row+i][col+j] == "#":
                    count += 1
            else:
                if visible_occupied_in_direction(board, row, col, i, j):
                    count += 1

    return count


def visible_occupied_in_direction(board, row, col, step_row, step_col):
    row += step_row
    col += step_col
    while 0 < row < len(board) - 1 and 0 < col < len(board[0]) - 1:
        if board[row][col] == "#":
            return True
        elif board[row][col] == "L":
            return False
        row += step_row
        col += step_col
    return False


def play(board, visible=False):
    rows = len(board)
    cols = len(board[0])
    add_border(board)
    changed = True
    round_no = 1
    while changed:
        board, changed = perform_round(board, rows, cols, visible)
        print_board(board)
        round_no += 1

    print(f"No change at round {round_no}")
    return board


def count_occupied(board):
    occupied = 0
    for row in board:
        for col in row:
            if col == "#":
                occupied += 1

    return occupied


board = play(data, visible=True)
print(f"Occupied: {count_occupied(board)}")


