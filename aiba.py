def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "-"]
]

print_board(board)