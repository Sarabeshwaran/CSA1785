Input:

import math
def minimax (curDepth, nodeIndex,
             maxTurn, scores,
             targetDepth):
    if (curDepth == targetDepth):
        return scores[nodeIndex]
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,
                    False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                    False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,
                     True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                     True, scores, targetDepth))
scores = [3, 5, 2, 9]
treeDepth = math.log(len(scores), 2)
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))

def game_over(state):
    # Return True if the game is over, False otherwise
    pass

def evaluate(state):
    # Evaluate the state of the game
    pass

def play(state, AI):
    while not game_over(state):
        # Human turn
        x, y = None, None
        while x is None and y is None:
            move = input("Your move (x y): ").strip().split()
            x, y = int(move[0]), int(move[1])
            if [x, y] not in empty_cells(state):
                print("Invalid move")
                x, y = None, None
        state[x][y] = "Human
        
        
Output:
  
The optimal value is : 3
