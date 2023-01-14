from EightPuzzle import *

GOAL_STATE = [[0,1,2],[3,4,5],[6,7,8]]
def h(s):
    h=0
    for i in range(3):
        for j in range(3):
            if s.b[i][j] != 0:
                if s.b[i][j] != GOAL_STATE[i][j]:
                    h+=1
    return h
