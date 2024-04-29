def generate_child(puzzle, level):
    def find_blank(puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if puzzle[i][j]=='_':
                    return i,j
    
    x, y = find_blank(puzzle)
    val_list = [(x,y-1,'left'),(x,y+1,'right'),(x-1,y,'up'),(x+1,y,'down')]
    children = []
    for x2, y2, direction in val_list:
        if 0<=x2<len(puzzle) and 0<=y2<len(puzzle):
            temp_puzzle = [row[:] for row in puzzle] #Create Shallow Copy of the puzzle
            temp_puzzle[x][y], temp_puzzle[x2][y2] = temp_puzzle[x2][y2], temp_puzzle[x][y] #Swap
            children.append((temp_puzzle, level+1, direction))
    return children


def misplaced_tiles(puzzle, goal):
    misplaced = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j]!=goal[i][j] and puzzle[i][j]!='_':
                misplaced+=1
    return misplaced

def solve_puzzle(start_state, goal_state, size):
    open_list = [(start_state, 0, 0)]
    closed_list = []

    while True:
        current_state, level, _ = open_list.pop(0)

        print("\nCurrent Puzzle State:")
        for row in current_state:
            print(' '.join(row))

        if misplaced_tiles(current_state, goal_state) == 0:
            print("Goal State reached!")
            break
        
        for child_state, child_level, direction in generate_child(current_state,level):
            if child_state not in [item[0] for item in open_list] and child_state not in [item[0] for item in closed_list]:
                open_list.append((child_state, child_level, direction))
                print(f"Move {direction} with f(n)={misplaced_tiles(child_state,goal_state)}+{child_level}={misplaced_tiles(child_state,goal_state)+child_level}")
        
        closed_list.append((current_state, level, 0))
        open_list.sort(key=lambda x: misplaced_tiles(x[0],goal_state)+x[1])

        if open_list:
            print(f"Chosen Action: Move {open_list[0][2]}")
        else:
            print("No more moves available")
            break

def accept_puzzle(size):
    puzzle = []
    for _ in range(size):
        row = input().split()
        puzzle.append(row)
    return puzzle

puzzle_size = 3
print("Enter the inital state:")
start_state = accept_puzzle(puzzle_size)
print("Enter goal state:")
goal_state = accept_puzzle(puzzle_size)

solve_puzzle(start_state, goal_state, puzzle_size)