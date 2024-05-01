def display_board(board):
    for i in range(0,9):
        if i%3==0:
            print("\n")
        if board[i]==0:
            print("_ ", end=" ")
        if board[i]==-1:
            print("X ", end=" ")
        if board[i]==1:
            print("O ", end=" ")

def user_turn(board):
    position = int(input("\nEnter a position to play[1-9]: "))
    if board[position-1]!=0:
        print("Wrong Move!")
        exit(0)
    board[position-1]=-1

def minimax(board, player,depth):
    result = analyze_board(board)
    if result!=0:
        return result*player/depth
    if depth>=9:
        return 0
    best_score=-2
    for i in range(0,9):
        if board[i]==0:
            board[i] = player
            score = -minimax(board, player*-1,depth+1)
            board[i]=0

            if score>best_score:
                best_score=score
    if best_score==-2:
        return 0
    return best_score

def computer_turn(board,depth):
    best_pos = -1
    best_score = -2
    print("Computer's possible moves with scores:")
    for i in range(0,9):
        if board[i]==0:
            board[i]=1
            score=-minimax(board,-1,depth+1)
            print(f"At position {i+1} computer scores {score}")
            board[i]=0

            if score>best_score:
                best_score=score
                best_pos=i
    board[best_pos]=1
    print(f"Computer chooses move {best_pos+1}")

def analyze_board(board):
    winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for c in winning_combinations:
        if board[c[0]]!=0 and board[c[0]]==board[c[1]] and board[c[1]]==board[c[2]]:
            return board[c[2]]
    return 0

print("Computer: O  vs  You: X\n")
board = [0]*9
player=int(input("Enter to play 1st or 2nd: "))
for i in range(0,9):
    if analyze_board(board)!=0:
        break
    if (i+player)%2==0:
        computer_turn(board,0)
    else:
        display_board(board)
        user_turn(board)

winner = analyze_board(board)
if winner==0:
    print("Its a draw")
elif winner==-1:
    print("User wins")
elif winner==1:
    print("computer wins")
