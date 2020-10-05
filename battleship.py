def starting_board(rows = 5, columns = 5):
    board = []
    for column in range(rows):
        board.append(["▉"] * columns)
    
    return board

def print_board(board):
    for row in board:
        print((" ").join(row))

def get_ship_place() #Pobieranie od uzytkownika miesca statków, zapisywanie i zwaracanie współrzędnych 
    pass

def get_player_move() #
    pass

def is_hit() 
    pass

def is_sunk()
    pass

def mark()
    pass

def has_won()
    pass

def print_result()
    pass 

def menu()
    pass 

def battleship_game()

# board; players1_ships; player2_ships; player_1_moves; player_2_moves

while has_won() == False





board = starting_board() 

print_board(board)


