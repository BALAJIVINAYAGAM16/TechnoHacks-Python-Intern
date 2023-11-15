board = [" " for x in range(9)]

def main(board):
    instructions = """Please read general instructions carefully:\n
           1.The game is played on a 3*3 grid 
                           
                     1 | 2 | 3
                    ---|---|---
                     4 | 5 | 6
                    ---|---|---  
                     7 | 8 | 9
                    
           2.Choose your symbol(X or O)
           3.Choose number to place a symbol(1-9)
           4.The player who get 3 of his/her marks in a row (up, down, across, or diagonally) is the winner."""
    print(instructions)
    
    def print_board():
        grid = f"""

        {board[0]}  | {board[1]} | {board[2]}
        ---|---|---
        {board[3]}  | {board[4]} | {board[5]}
        ---|---|---
        {board[6]}  | {board[7]} | {board[8]}

        """

        print(grid)
    
    player1 = str(input("Enter player1 name:"))
    player2 = str(input("Enter player2 name:"))

        
    def player_move(icon):
        if icon == "X":
            player = f"{player1}"
        elif icon == "O":
            player = f"{player2}"
        print(f"Your turn player {player}")
        choice = int(input("Enter your move (1-9): "))
        if board[choice - 1] == " ":
            board[choice - 1] = icon
        else:
            print("That space is already taken!")

    def is_victory(icon):
        if ((board[0] == icon and board[1] == icon and board[2] == icon) or 
        (board[3] == icon and board[4] == icon and board[5] == icon) or 
        (board[6] == icon and board[7] == icon and board[8] == icon) or 
        (board[0] == icon and board[3] == icon and board[6] == icon) or 
        (board[1] == icon and board[4] == icon and board[7] == icon) or 
        (board[2] == icon and board[5] == icon and board[8] == icon) or 
        (board[0] == icon and board[4] == icon and board[8] == icon) or 
        (board[2] == icon and board[4] == icon and board[6] == icon)):
            return True
        else:
            return False

    def is_draw():
        if " " not in board:
            return True
        else:
            return False

    while True:
        print_board()
        player_move("X")
        print_board()
        if is_victory("X"):
            print(f"{player1} wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
        player_move("O")
        if is_victory("O"):
            print_board()
            print(f"{player2} wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break

main(board)