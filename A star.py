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
# A* algorithm implemented for the sliding puzzle game:

# The sliding puzzle game is a classic puzzle game where the player must rearrange numbered 
# tiles within a grid by sliding them into the empty space until they are in a specific predefined order.

# The astar_sliding_puzzle function is the main function that implements the A* algorithm for the sliding puzzle game.
# It takes the start_state and target_state as inputs.

# The moves variable defines the possible moves in the puzzle, which include moving tiles to the right, down, left, and up.

# The get_heuristic function calculates the heuristic value for a given state. In the sliding puzzle game, the heuristic is
# calculated as the sum of the Manhattan distances between each tile and its target position (ignoring the blank tile).

# The generate_next_states function generates the possible next states given a current state. It checks the empty cell's 
# neighboring positions and swaps the empty cell with a neighboring tile to create a new state. It returns a list of all the possible next states.

# The get_empty_cell function finds the position of the empty cell (represented by the value 0) in a given state.

# The open_set is a priority queue that stores the states to be explored. Each state is a tuple containing the heuristic value
# and the state itself. It is initially populated with the start state.

# The g_scores dictionary stores the cost to reach each state from the start state.

# The A* algorithm's main loop starts with a priority queue that retrieves the state with the lowest heuristic value (priority) 
# from the open_set.

# If the current state is equal to the target state, a solution has been found, and the function returns True.

# If the current state is not the target state, the algorithm generates the possible next states using the generate_next_states
# function.

# For each next state, the g_score is calculated as the cost to reach the current state plus one.

# If the g_score for the next state is lower than the existing g_score (or infinity if no g_score exists), the g_scores 
# dictionary is updated, and the next state is added to the open_set with its priority calculated as the sum of g_score and the heuristic value.

# If the open_set becomes empty, it means no solution is found, and the function returns False.

# After the main loop, the astar_sliding_puzzle function is called with the start and target states, and the return value
# is stored in the is_solvable variable.

# Finally, based on the value of is_solvable, the program prints whether the puzzle is solvable 
# or not.


import heapq

class NumberPuzzle:
    def __init__(self, start_state, target_state):
        self.start_state = start_state
        self.target_state = target_state
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_heuristic(self, state):
        # Calculate the heuristic value as the number of misplaced tiles
        return sum(state[i][j] != self.target_state[i][j] for i in range(len(state)) for j in range(len(state[0])))

    def generate_next_states(self, state):
        # Generate the possible next states by swapping the empty cell with its neighboring tiles
        next_states = []
        empty_row, empty_col = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)
        for move in self.moves:
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
                # Swap the empty cell with a neighboring tile
                new_state = [row.copy() for row in state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
                next_states.append(new_state)
        return next_states

    def solve(self):
        open_set = [(self.get_heuristic(self.start_state), self.start_state)]
        g_scores = {tuple(map(tuple, self.start_state)): 0}
        while open_set:
            _, current_state = heapq.heappop(open_set)
            if current_state == self.target_state:
                # Target state is found, puzzle is solvable
                return True
            for next_state in self.generate_next_states(current_state):
                g_score = g_scores[tuple(map(tuple, current_state))] + 1
                if g_score < g_scores.get(tuple(map(tuple, next_state)), float('inf')):
                    # Update g_score if a better path is found
                    g_scores[tuple(map(tuple, next_state))] = g_score
                    heapq.heappush(open_set, (g_score + self.get_heuristic(next_state), next_state))
        # No solution found, puzzle is not solvable
        return False

# Define the start and target states
start_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Create a NumberPuzzle instance
puzzle = NumberPuzzle(start_state, target_state)

# Solve the puzzle
is_solvable = puzzle.solve()

# Print the result
if is_solvable:
    print("The puzzle is solvable!")
else:
    print("No solution found.")
