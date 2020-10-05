def starting_board(rows = 5, columns = 5):
    board = []
    for column in range(rows):
        board.append(["▉"] * columns)
    
    return board

def print_board(board):
    for row in board:
        print((" ").join(row))

board = starting_board(8,5) 
print_board(board)