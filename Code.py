game = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],  # the board
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solver(board):
    find = find_square(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):  # checks with all values
        if checker(board, i, (row, col)):
            board[row][col] = i

            if solver(board):  # Backtracks
                return True

            board[row][col] = 0

    return False


def checker(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:  # Row check
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:  # Column check
            return False
    # box divides value by 3 so each 3x3 box is treated as one element
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):  # 3x3 square check
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def print_game_board(board):  # prints the board
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('----------------------------')
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print('|', end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end=" ")


def find_square(board):  # finds and returns coordinates of cell with value 0(empty)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j  # y,x
    return None


print_game_board(game)
solver(game)
print("*******************************")
print_game_board(game)
