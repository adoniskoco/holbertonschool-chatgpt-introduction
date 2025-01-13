def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        
        
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid row or column. Please enter values between 0 and 2.")
                    continue
                
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("That spot is already taken! Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")
        
        
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        
        player = "O" if player == "X" else "X"


tic_tac_toe()