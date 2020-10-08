import os

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
    
    
def get_ship_place(): 
    # Prosi o postawienie 4 statków (powietrznych) - następnie zwraca tablice z ustawieniami.
    ship_list = []
    board = starting_board()
    while len(ship_list) != 3:
        try:
            print_board(board)
            column_number = int(input("Enter row number: "))
            row_number = int(input("Enter column number:"))
            if column_number in range(len(board[0]) + 1) and row_number in range(len(board) + 1):
                if [column_number - 1,row_number - 1] not in ship_list:   
                    ship_list.append([column_number - 1,row_number - 1]) 
                else:
                    print("Place already taken!")
            else:
                print("Enter valid coordinates!")
            for i in ship_list:
                board[i[0]][i[1]] = "✈"
            input("Press enter to continue.")
            os.system("cls || clear")
        except:
            print("Only numbers!")
    return board
    

def get_player_move(player_moves): 
    # Bierze tablice ruchów gracza i sprawdza czy ruch jest możliwy do wykonania, jeśli tak zwraca koordynaty - najlepiej do funkcji is_hit i is_sunk!
    while True:
        print_board(player_moves)
        try:
            column_number = int(input("Column number: "))
            row_number = int(input("Row number: "))

            if player_moves[row_number][column_number] == '▉': 
                return row_number, column_number
            else: 
                input("Pleas enter valid move!")
            input("Press enter to continue.")
            os.system("cls || clear")
        except: 
            input("Enter only numbers!")
  
    
def is_hit(player_X_ship, player_Y_moves, coordinates): 
    # powinna brać tablice player_X_ships i koordynaty z get_player_move i zwracać hit lub miss na tablicy  player_Y_moves
    pass

def is_sunk():
    # na razie nie potrzebna
    pass

def mark():
    # is_hit bierze to na siebie
    pass

def has_won(players_1_ships, player_2_ships, player_1_moves, player_2_moves):
    # porównuje tablice player_X_ships z tablicą player_Y_moves - jeśli wszystkie cele są zastrzelone zwraca True 
    return False

def print_result():
    pass 

def menu():
    pass 

def battleship_game():

# board; players_1_ships; player_2_ships; player_1_moves; player_2_moves

    player_1_moves = starting_board()
    player_2_moves = starting_board()
    input("Player 1 - Press Enter ")
    player_1_ships = get_ship_place()
    input("Player 2 - Press Enter  ")
    player_2_ships = get_ship_place()

    while has_won(player_1_ships, player_2_ships, player_1_moves, player_2_moves) == False:
        input("Player 1 - Press Enter ")
        is_hit(player_2_ships, player_1_moves, get_player_move(player_1_moves))
        input("Player 2 - Press Enter ")
        is_hit(player_1_ships, player_2_moves, get_player_move(player_2_moves))

        
battleship_game()     










