from EightPuzzle import *

def h(s):
    h=0
    for t in [1,2,3,4,5,6,7,8]:
        for i in range(3):
            for j in range(3):
                if s.b[i][j] == t:
                    h += abs(i - (t//3)) + abs(j - (t%3))
    return h