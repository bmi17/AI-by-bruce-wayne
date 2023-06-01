#  Implement A star Algorithm for any game search problem.


# 1.  sanu's code 
import copy

# Define the final state and initial state of the puzzle
final = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
initial = [[1, 2, 3], [-1, 4, 6], [7, 5, 8]]

# Function to find the heuristic cost
def gn(state, finalstate):
    count = 0
    for i in range(3):
        for j in range(3):
            # Check if the tile is not the blank tile (-1)
            if state[i][j] != -1:
                # Increment the count if the tile value is not equal to the final state value at the same position
                if state[i][j] != finalstate[i][j]:
                    count += 1
    return count

# Function to find the position of the blank cell (-1)
def findposofblank(state):
    for i in range(3):
        for j in range(3):
            # Return the position of the blank cell if found
            if state[i][j] == -1:
                return [i, j]

# Function to move the blank cell to the left
def move_left(state, pos):
    if pos[1] == 0:
        return None
    retarr = copy.deepcopy(state)
    # Swap the blank cell with the left cell
    retarr[pos[0]][pos[1]], retarr[pos[0]][pos[1] - 1] = retarr[pos[0]][pos[1] - 1], retarr[pos[0]][pos[1]]
    return retarr

# Function to move the blank cell up
def move_up(state, pos):
    if pos[0] == 0:
        return None
    retarr = copy.deepcopy(state)
    # Swap the blank cell with the upper cell
    retarr[pos[0]][pos[1]], retarr[pos[0] - 1][pos[1]] = retarr[pos[0] - 1][pos[1]], retarr[pos[0]][pos[1]]
    return retarr

# Function to move the blank cell to the right
def move_right(state, pos):
    if pos[1] == 2:
        return None
    retarr = copy.deepcopy(state)
    # Swap the blank cell with the right cell
    retarr[pos[0]][pos[1]], retarr[pos[0]][pos[1] + 1] = retarr[pos[0]][pos[1] + 1], retarr[pos[0]][pos[1]]
    return retarr

# Function to move the blank cell down
def move_down(state, pos):
    if pos[0] == 2:
        return None
    retarr = copy.deepcopy(state)
    # Swap the blank cell with the lower cell
    retarr[pos[0]][pos[1]], retarr[pos[0] + 1][pos[1]] = retarr[pos[0] + 1][pos[1]], retarr[pos[0]][pos[1]]
    return retarr

# Function to print the matrices array
def printMatrix(matricesArray):
    print("")
    counter = 1
    for matrix in matricesArray:
        print("Step {}".format(counter))
        for row in matrix:
            print(row)
        counter += 1
        print("")

# Function to solve the 8-puzzle
def eightPuzzle(initialstate, finalstate):
    hn = 0
    explored = []
    while True:
        explored.append(initialstate)
        if initialstate == finalstate:
            break
        hn += 1
        # Generate all possible moves from the current state
        left = move_left(initialstate, findposofblank(initialstate))
        right = move_right(initialstate, findposofblank(initialstate))
        up = move_up(initialstate, findposofblank(initialstate))
        down = move_down(initialstate, findposofblank(initialstate))
        # Calculate the heuristic cost for each move
        fnl = 1000
        fnr = 1000
        fnu = 1000
        fnd = 1000
        if left != None:
            fnl = hn + gn(left, finalstate)
        if right != None:
            fnr = hn + gn(right, finalstate)
        if up != None:
            fnu = hn + gn(up, finalstate)
        if down != None:
            fnd = hn + gn(down, finalstate)
        # Choose the move with the minimum heuristic cost
        minfn = min(fnl, fnr, fnu, fnd)
        if (fnl == minfn) and (left not in explored):
            initialstate = left
        elif (fnr == minfn) and (right not in explored):
            initialstate = right
        elif (fnu == minfn) and (up not in explored):
            initialstate = up
        elif (fnd == minfn) and (down not in explored):
            initialstate = down
    # Print the explored matrices
    printMatrix(explored)

# Main function
def main():
    while True:
        ch = int(input("PRESS 1 to continue and 0 to Exit : "))
        if not ch:
            break
        start = []
        print("START STATE\n")
        for i in range(3):
            arr = []
            for j in range(3):
                a = int(input("Enter element at  {},{}: ".format(i, j)))
                arr.append(a)
            start.append(arr)
        final = []
        print("FINAL STATE\n")
        for i in range(3):
            arr = []
            for j in range(3):
                a = int(input("Enter element at  {},{}: ".format(i, j)))
                arr.append(a)
            final.append(arr)
        eightPuzzle(start, final)

# Call the main function
main()



# 2. second code ( for myself)
g = 0  # Global variable to keep track of the number of moves

# Function to print the puzzle board
def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()  # Start a new line for every 3 elements
        if elements[i] == -1:
            print("_", end=" ")  # Print "_" for the empty space
        else:
            print(elements[i], end=" ")  # Print the number for non-empty spaces
    print()  # Start a new line after printing the board


# Function to check if the puzzle is solvable
def solvable(start):
    inv = 0

    for i in range(9):
        if start[i] <= 1:
            continue
        for j in range(i + 1, 9):
            if start[j] == -1:
                continue
            if start[i] > start[j]:
                inv += 1
    if inv % 2 == 0:
        return True  # Solvable if the number of inversions is even
    return False


# Function to calculate the heuristic value for a state
def heuristic(start, goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:
                h += (abs(j - i)) // 3 + (abs(j - i)) % 3
    return h + g


# Functions to move the empty space in different directions
def moveleft(start, position):
    start[position], start[position - 1] = start[position - 1], start[position]


def moveright(start, position):
    start[position], start[position + 1] = start[position + 1], start[position]


def moveup(start, position):
    start[position], start[position - 3] = start[position - 3], start[position]


def movedown(start, position):
    start[position], start[position + 3] = start[position + 3], start[position]


# Function to determine the best move for the empty space
def movetile(start, goal):
    emptyat = start.index(-1)
    row = emptyat // 3
    col = emptyat % 3
    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1, f2, f3, f4 = 100, 100, 100, 100

    if col - 1 >= 0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col + 1 < 3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 < 3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row - 1 >= 0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2, f3, f4)

    if f1 == min_heuristic:
        moveleft(start, emptyat)
    elif f2 == min_heuristic:
        moveright(start, emptyat)
    elif f3 == min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)


# Function to solve the 8-puzzle using A* search algorithm
def solveEight(start, goal):
    global g
    g += 1
    movetile(start, goal)
    print_board(start)  # Print the current state of the puzzle board
    f = heuristic(start, goal)
    if f == g:
        print("Solved in {} moves".format(f))
        return

    solveEight(start, goal)  # Recursively call the function to continue solving


# Main function
def main():
    global g
    start = list()
    goal = list()
    print("Enter the start state:(Enter -1 for empty):")
    for i in range(9):
        start.append(int(input()))  # Read the start state input from the user

    print("Enter the goal state:(Enter -1 for empty):")
    for i in range(9):
        goal.append(int(input()))  # Read the goal state input from the user

    print_board(start)  # Print the initial state of the puzzle board

    # Check if the puzzle is solvable
    if solvable(start):
        solveEight(start, goal)  # Solve the puzzle
        print("Solved in {} moves".format(g))
    else:
        print("Not possible to solve")


if __name__ == '__main__':
    main()



# Test Cases
# 
# 1
# 2
# 3
# -1
# 4 
# 6
# 7 
# 5 
# 8 

# 1 
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8
# -1




# # The code you provided appears to be an implementation of the A* search algorithm for solving the 8-puzzle problem. 
# The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one empty space. The goal is to rearrange the tiles from a given start state to a desired goal state by sliding them into the empty space.

# # The code includes several functions:

# # 1. `print_board(elements)`: This function is used to print the current state of the puzzle board in a human-readable format.

# # 2. `solvable(start)`: This function checks whether a given start state of the puzzle is solvable or not.
# It uses the concept of inversion count to determine solvability. If the number of inversions (the number of tiles that are out of their natural order) is even, the puzzle is solvable.

# # 3. `heuristic(start, goal)`: This function calculates the heuristic value (h) for a given state by counting 
# the number of misplaced tiles in the current state compared to the goal state. It uses the Manhattan distance heuristic, which calculates the minimum number of moves required for each tile to reach its goal position.

# # 4. `moveleft(start, position)`, `moveright(start, position)`, `moveup(start, position)`, `movedown(start, position)
# `: These functions are used to move the empty space (represented by -1) in the puzzle board left, right, up, or down, respectively.

# # 5. `movetile(start, goal)`: This function determines the best move for the empty space by calculating the heuristic 
# values for each possible move. It selects the move that minimizes the heuristic value.

# # 6. `solveEight(start, goal)`: This function implements the A* search algorithm to solve the puzzle. It repeatedly
# calls the `movetile` function to make moves until the puzzle reaches the goal state. It also keeps track of the number of moves (g) made to reach the current state.

# # 7. `main()`: This is the main function that takes user input for the start and goal states of the puzzle and calls the
# necessary functions to solve it.

# # To use the code, you can enter the start and goal states of the 8-puzzle as input. The start and goal states should be 
# entered as a sequence of 9 numbers, where -1 represents the empty space. After entering the input, the code will attempt to solve the puzzle and display the steps taken to reach the goal state.

# # Note that the code does not include any error handling or input validation, so it assumes correct and valid input from 
# the user.
