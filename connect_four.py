'''
Connect 4 
Solution to: Programming 2, task 1
Author:Elmer Dema
Kudos to: https://www.youtube.com/watch?v=Z5xNDIYb7eI&t=1294s&ab_channel=ShefsofProblemSolving

'''

rows = 6
columns = 7
board = [[0 for i in range(columns)] for j in range(rows)]
PLAYER1 = 1
PLAYER2 = 2
game_on= True
player_turn = 1

print("WELCOME TO CONNECT FOUR")
print("If you want to restart type k")
print("If you want to quit type q")
#checks whether the row is empty(x=0), if it is, it places the sign in the row
def move(board,move,sign):
    for i in range(rows):
        x=board[rows-i-1][move]
        if x==0:
            board[rows-i-1][move]=sign
            break
    return board


def board_style(board):
      
    for i in board:
        print(f"| {i} |")
        print("----------------------------")    


def check_win_row(board, row_placement, column_placement):
    start = board[row_placement][column_placement]
    count = 1
    # checks to the left
    for i in range(3):
        col = column_placement - 1 - i
        if col >= 0:
            current = board[row_placement][col]
            if current == start:
                count += 1
                if count == 4:
                    return True
            else:
                break
        else:
            break
    if count == 4:
        return True
    # checks to the right    
    for i in range(4 - count):
        col = column_placement + 1 + i
        if col < columns:
            current = board[row_placement][col]
            if current == start:
                count += 1
                if count == 4:
                    return True
            else:
                break
        else:
            break
    return False


def check_win_column(board,row_placement,column_placement):
    start = board[row_placement][column_placement]
    count = 1
    for i in range(rows):
        #checks if the row is in the board
        if i != row_placement and board[i][column_placement] == start:
            count += 1
            if count == 4:
                return True
        else:
            count = 1
    return False


def check_win_diagonal(board,row_placement,column_placement):
    start=board[row_placement][column_placement]
    count=1
    #i and j are const diagonal
    #go to the left and down
    for i in range(3):
        row=row_placement+i+1
        col=column_placement-i-1
        #used to check if the row and column are in the board
        if row<rows and col>-1:
            current=board[row][col]
            if current==start:
                count+=1
            else:
                break
        else:
            break
    #right and up    
    if count==4:
        return True    
    for i in range(4-count):
        row=row_placement-i-1
        col=column_placement+i+1
        #check if we are in the board
        if row>-1 and col<columns:
            current=board[row][col]
            if current==start:
                count+=1
            else:
                break
        else:
            break
    if count==4:
        return True
    #new count for other diagonals
    #i - j is const diagonal
    count=1
    #go to the left and up
    for i in range(3):
        row=row_placement-i-1
        col=column_placement-i-1
        #used to check if the row and column are in the board
        if row<rows and col>-1:
            current=board[row][col]
            if current==start:
                count+=1
            else:
                break
        else:
            break
    #right and down   
    for i in range(4-count):
        row=row_placement+i+1
        col=column_placement+i+1
        #check if we are in the board
        if row<rows and col<columns:
            current=board[row][col]
            if current==start:
                count+=1
            else:
                break
        else:
            break
    if count==4:
        return True     
    return False


def check_draw(board):
    for row in board:
        if 0 in row:
            return False
    return True

#If one of the functions returns true, the game ends
def check_win(board,move):
    #figures out the position of the last move
    for i in range(rows):
        current=board[rows-1-i][move]
        if current==0:
            break
    row_placement=rows-i
    column_placement=move
    return check_win_column(board,row_placement,column_placement) or check_win_row(board,row_placement,column_placement) or check_win_diagonal(board,row_placement,column_placement) or check_draw(board)

def winner(player_turn):
    print("Player "+str(3 - player_turn)+" won the game")

while game_on == True:
    #asks the player to enter a move (digit)
    user_input = input("Player "+str(player_turn)+" enter a move: ")
    if user_input.isdigit() and int(user_input) > -1 and int(user_input) < 7:    
        move_num = int(user_input)
        #check if the column is full
        if board[0][move_num] != 0:
            print("Column is full")
            continue    
        if move_num == -1:
            break
        board = move(board, move_num, player_turn)
        board_style(board)
        player_turn = 3 - player_turn
        game_on = not check_win(board, move_num)
        if not game_on:
            winner(player_turn)
        #asks the player whether they want to restart
    elif user_input.lower() == "k":
        print("Game has been restarted")
        board = [[0 for i in range(columns)] for j in range(rows)]
        board_style(board)
        player_turn = 1
        game_on = True
    elif user_input.lower() == "q":
        print("Game has been quit")
        break   