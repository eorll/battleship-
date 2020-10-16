import os

def starting_board(rows, columns):
    board = []
    for column in range(rows):
        board.append(["\u001b[34;1m▉\u001b[0m"] * columns)
    
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
    
    
def get_ship_place(double_ships, single_ships,rows, columns): 
    # Prosi o postawienie statków (powietrznych) - następnie zwraca tablice z ustawieniami.
    ship_list = []
    forbidden_places = []
    board = starting_board(rows, columns)
    input(f"Put {double_ships} double ships!")
    while len(ship_list) != (double_ships * 2):
        ship_placement(board, ship_list, forbidden_places, ship_place_coordinates(board,'double'))

    input(f"Put {single_ships} single ships! ")
    while len(ship_list) != (double_ships * 2 + single_ships):
        ship_placement(board, ship_list, forbidden_places, ship_place_coordinates(board,None))
    
    return board


def ship_place_coordinates(board,ship_type):
    while True:
        try:
            os.system("cls || clear")
            print_board(board)
            row_number = int(input("Enter column number:"))
            column_number = int(input("Enter row number: "))
            xy_1 = [column_number - 1,row_number - 1]
            if ship_type == None:

                return xy_1
            else:
                while True:
                    ship_position = input("Enter ship position (H/orizontial or V/ertical): ").upper()
                    if ship_position == 'H' or ship_position == 'V':
                        if ship_position == "H":
                            xy_2 = [column_number, row_number - 1]
                        elif ship_position == "V":
                            xy_2 = [column_number - 1,row_number]
                        return [xy_1, xy_2]
                    else:
                        input("Enter valid position! H or V")
        except:
            input("Use only numbers!")   

def ship_placement(board, ship_list, forbidden_places, ship_coordinates):
    
    try:
    
        if (ship_coordinates[0] and ship_coordinates[1]) not in forbidden_places:
            if ((ship_coordinates[0][0] and ship_coordinates[0][1]) in range(len(board[0]))) and ((ship_coordinates[1][0] and ship_coordinates[1][1]) in range((len(board)))):
                if (ship_coordinates[0] and ship_coordinates[1]) not in ship_list:   
                    ship_list.append(ship_coordinates[0]) 
                    ship_list.append(ship_coordinates[1]) 
                    taken_places(forbidden_places,ship_coordinates[0][0], ship_coordinates[0][1])
                    taken_places(forbidden_places,ship_coordinates[1][0], ship_coordinates[1][1])
                else:
                    input("Place already taken!")
            else:
                input("Enter valid coordinates!")
        else:
            input("Too close to another ship!")
    except:
        
        if ship_coordinates not in forbidden_places:
            if ship_coordinates[0] in range((len(board[0]))) and ship_coordinates[1] in range((len(board))):
                if ship_coordinates not in ship_list:   
                    ship_list.append(ship_coordinates) 
                    taken_places(forbidden_places,ship_coordinates[0], ship_coordinates[1])
                else:
                    input("Place already taken!")
            else:
                input("Enter valid coordinates!")
        else:
            input("Too close to another ship!")

    for i in ship_list:
        board[i[0]][i[1]] = "✈"
    os.system("cls || clear")
        
    print_board(board)
    input("Press enter")    
    os.system("cls || clear")   
    return board


def taken_places(forbidden_places,x, y):
    # zapewnia 1 pole odstępu pomiędzy statkami

    forbidden_places.append([x-1,y-1])
    forbidden_places.append([x,y-1])
    forbidden_places.append([x+1,y-1])
    forbidden_places.append([x-1,y])
    forbidden_places.append([x+1,y])
    forbidden_places.append([x-1,y+1])
    forbidden_places.append([x,y+1])
    forbidden_places.append([x+1,y+1])

    return forbidden_places

    

def get_player_move(player_moves): 
    # Bierze tablice ruchów gracza i sprawdza czy ruch jest możliwy do wykonania, jeśli tak zwraca koordynaty - najlepiej do funkcji is_hit i is_sunk!
    while True:
        print_board(player_moves)
        try:
            column_number = int(input("Column number: "))
            row_number = int(input("Row number: "))

            if player_moves[row_number - 1][column_number - 1] == '\u001b[34;1m▉\u001b[0m': 
                return [row_number -1, column_number -1]
            else: 
                input("Pleas enter valid move!")
            os.system("cls || clear")
        except: 
            input("Enter only numbers!")
  
    
def is_hit(player_X_ship, player_Y_moves, coordinates): 
    # powinna brać tablice player_X_ships i koordynaty z get_player_move i zwracać hit lub miss na tablicy  player_Y_moves ≋ ☠ ♨
    arround_places = []
    taken_places(arround_places,coordinates[0], coordinates[1])
    if player_X_ship[coordinates[0]][coordinates[1]] == "✈":
        player_Y_moves[coordinates[0]][coordinates[1]] = '\u001b[31m☠\u001b[0m'
        os.system("cls || clear")
        print_board(player_Y_moves)
        print('     HIT')
        for i in arround_places:
            if player_X_ship[i[0]][i[1]] == "✈":
                player_Y_moves[coordinates[0]][coordinates[1]] = '♨'
                os.system("cls || clear")
                print_board(player_Y_moves)
                print('     HIT')
                if  player_Y_moves[i[0]][i[1]] == '♨':
                    player_Y_moves[i[0]][i[1]] = '\u001b[31m☠\u001b[0m' 
                    player_Y_moves[coordinates[0]][coordinates[1]] = '\u001b[31m☠\u001b[0m'
                    os.system("cls || clear")
                    print_board(player_Y_moves)
                    print('     BOOM')       
    else:
        player_Y_moves[coordinates[0]][coordinates[1]] = '≋'
        os.system("cls || clear")
        print_board(player_Y_moves)
        print("     MISS")

    return player_Y_moves


def has_won(player_X_ships, player_Y_moves):
    move_test = []
    ship_test = []

    for i in player_Y_moves:
        for j in i:
            if j == '\u001b[31m☠\u001b[0m':
                move_test.append('\u001b[31m☠\u001b[0m')

    for i in player_X_ships:
        for j in i:
            if j == '✈':
                ship_test.append('\u001b[31m☠\u001b[0m')
    
    if move_test == ship_test:
        return True
    else:
        return False


def menu():
    rows = 5
    columns = 5
    double_ships = 1
    single_ships = 1
    while True:
        os.system("cls || clear")
        print("""        1 - Start Game
        2 - Change board size
        3 - Change number of ships
        """)
        option = input('Enter number:')
        
        if option == '1':
            battleship_game(rows, columns, double_ships, single_ships)
        if option == '2':
            try:
                rows = int(input('Enter number of rows: '))
                columns = int(input("Enter number of columns: "))
            except:
                input("Use only numbers!")

        if option == '3':
            try:
                double_ships = int(input("Enter numbers of double ships: "))
                single_ships = int(input("Enter numbers od single ships: "))
            except:
                input("USE ONLY NUMBERS!")

        

    pass 

def battleship_game(rows, columns, double_ships, single_ships):

# board; players_1_ships; player_2_ships; player_1_moves; player_2_moves

    player_1_moves = starting_board(rows, columns)
    player_2_moves = starting_board(rows, columns)
    input("Player 1 - Press Enter ")
    player_1_ships = get_ship_place(double_ships, single_ships,rows, columns)
    input("Player 2 - Press Enter  ")
    player_2_ships = get_ship_place(double_ships, single_ships,rows, columns)

    while True:
        
        input("Player 1 - Press Enter ")
        os.system("cls || clear")
        is_hit(player_2_ships, player_1_moves, get_player_move(player_1_moves))
        if has_won(player_2_ships,player_1_moves) == True:
            print('Player 1 - WON')
            break
        
        input("Player 2 - Press Enter ")
        os.system("cls || clear")
        is_hit(player_1_ships, player_2_moves, get_player_move(player_2_moves))
        if has_won(player_1_ships,player_2_moves) == True:
            print('Player 2 - WON')
            break

        
def main():
    
    menu()

main()








