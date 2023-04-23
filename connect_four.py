rows=6
columns=7
board=[[0 for i in range(columns)] for j in range(rows)]
PLAYER1=1
PLAYER2=2
game_over=False
player_turn=1

def move(board,move,sign):
    for i in range(rows):
        x=board[rows-i-1][move]
        if x==0:
            board[rows-i-1][move]=sign
            break
    return board

def board_style(board):
    for i in board:
        print(i)

while game_over==False:
    user_input=int(input("Player "+str(player_turn)+" enter a move: "))
    if move==1:
        break
    board=move(board,user_input,player_turn)
    board_style(board)
    player_turn=3-player_turn
