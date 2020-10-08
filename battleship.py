def starting_board(rows = 5, columns = 5):
    board = []
    for column in range(rows):
        board.append(["▉"] * columns)
    
    return board

def print_board(board):
    column_number = []
    n = 0
    for i in board[0]:
        n += 1 
        column_number.append(str(n))
        column_number.append(' ')

    print("  "+"".join(column_number))
    row_number = 1
    for row in board:
        print((str(row_number)) + " " + (" ").join(row))
        row_number += 1
    

def get_ship_place(): #Pobieranie od uzytkownika miesca statków, zapisywanie i zwaracanie współrzędnych 
    pass

def get_player_move(): 
    pass

def is_hit(): 
    pass

def is_sunk():
    pass

def mark():
    pass

def has_won():
    pass

def print_result():
    pass 

def menu():
    pass 

def battleship_game():

# board; players_1_ships; player_2_ships; player_1_moves; player_2_moves

    player_1_moves = starting_board()
    player_2_moves = starting_board()
    players_1_ships = get_ship_place()
    player_2_ships = get_ship_place()

    while has_won() == False:
        
        break
        










