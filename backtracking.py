from typing import List

# this is the helper function 
def solveNQueens( n: int ) -> List[List[str]]:
    col = set()
    posDiag = set() # (r + c)
    negDiag = set() # (r - c)

    # result matrix 
    res = []

    # board
    board = [["."]* n for i in range(n)]

    # Recursive HOF 
    def backtrack(r : int):
        ''' Row n is our Base Case '''

        if(r == n):
            copy = [ "".join(row) for row in board] 
            res.append(copy)

        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue # we will skip this position as it is attacked by the queen 
            
            # adding the sets
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = 'Q'

            # recurse
            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."
    
    # calling the backtrack function 
    backtrack(0) # using row 0
    return res 

if __name__ == "__main__": 
    print("------------------------------------------------------------------------")
    for i in range(14): 
        print(f"{i} x {i} board possible solutions : {len(solveNQueens(i))}")
    print("------------------------------------------------------------------------")
