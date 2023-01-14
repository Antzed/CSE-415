""" AStar.py

A* Search of a problem space.
Partnership? (YES or NO): YES

CSE 415, Autumn 2022, University of Washington

This code contains my implementation of the A* Search algorithm.

Usage:
python3 AStar.py FranceWithDXHeuristic
"""

import sys
import importlib
from PriorityQueue import My_Priority_Queue


class AStar:
    """
    Class that implements A* Search for any problem space (provided in the required format)
    """
    def __init__(self, problem):
        """ Initializing the AStar class.
        Please DO NOT modify this method. You may populate the required instance variables
        in the other methods you implement.
        """
        self.Problem = importlib.import_module(problem)
        self.COUNT = None  # Number of nodes expanded.
        self.MAX_OPEN_LENGTH = None  # How long OPEN ever gets.
        self.PATH = None  # List of states from initial to goal, along lowest-cost path.
        self.PATH_LENGTH = None  # Number of states from initial to goal, along lowest-cost path.
        self.TOTAL_COST = None  # Sum of edge costs along the lowest-cost path.
        self.BACKLINKS = {}  # Predecessor links, used to recover the path.
        self.OPEN = None  # OPEN list
        self.CLOSED = None  # CLOSED list
        self.VERBOSE = True  # Set to True to see progress; but it slows the search.

        # The value g(s) represents the cost along the best path found so far
        # from the initial state to state s.
        self.g = {}  # We will use a hash table to associate g values with states.
        self.h = None  # Heuristic function

        print("\nWelcome to A*.")

    def runAStar(self):
        # Comment out the line below when this function is implemented.
        #raise NotImplementedError
        initial_state = self.Problem.CREATE_INITIAL_STATE()
        self.h = self.Problem.h
        print("Initial State:")
        print(initial_state)

        self.COUNT = 0
        self.MAX_OPEN_LENGTH = 0
        self.BACKLINKS = {}

        self.AStar(initial_state)
        print(f"Number of states expanded: {self.COUNT}")
        print(f"Maximum length of the open list: {self.MAX_OPEN_LENGTH}")

        #print("The CLOSED list is: ", ''.join([str(s)+' ' for s in CLOSED]))

    def AStar(self, initial_state):
        """AStar Search: This is the actual algorithm."""
        self.CLOSED = []
        self.BACKLINKS[initial_state] = None

        # STEP 1. For the start state s0, compute f(s0) = g(s0)+h(s0) = h(s0) and put [s0,f(s0)] on a list (priority queue)
        # OPEN.
        self.OPEN = My_Priority_Queue()
        self.OPEN.insert(initial_state, self.h(initial_state))
        # STEP 1.1. Assign g=0 to the start state.
        self.g[initial_state] = 0.0

        # STEP 2. If OPEN is empty, output “DONE” and stop.
        while len(self.OPEN) > 0:
            if self.VERBOSE:
                report(self.OPEN, self.CLOSED, self.COUNT)
                print("Before")
                txt = "OPEN: "
                for (s, q) in self.OPEN.q:
                    txt += "(" + str(s) + ", " + str(q) + "), "
                print("\n" + txt)

                txt = "CLOSED: "
                for (s, q) in self.CLOSED:
                    txt += "(" + str(s) + ", " + str(q) + "), "
                print(txt)
            if len(self.OPEN) > self.MAX_OPEN_LENGTH:
                self.MAX_OPEN_LENGTH = len(self.OPEN)

            # STEP 3 Find and remove the item [s,p] on OPEN having lowest p. Break ties arbitrarily
            # Put [s,p] on CLOSED.

            (S, P) = self.OPEN.delete_min()
            #print("In Step 3, returned from OPEN.delete_min with results (S,P)= ", (str(S), P)) ##????
            """txt = "CLOSED: "
            for (s,q) in self.CLOSED:
                txt += "(" + str(s) + ", " + str(q) + "), "
            print (txt)"""
            self.CLOSED.append((S, P))

            # STEP 3.1 If s is a goal state: output its description (and backtrace a path), and
            # if h is known to be admissible, halt.
            if self.Problem.GOAL_TEST(S):
                print(self.Problem.GOAL_MESSAGE_FUNCTION(S))
                self.PATH = [str(state) for state in self.backtrace(S)]
                self.PATH_LENGTH = len(self.PATH) - 1
                print(f'Length of solution path found: {self.PATH_LENGTH} edges')
                self.TOTAL_COST = self.g[S]
                print(f'Total cost of solution path found: {self.TOTAL_COST}')
                return
            self.COUNT += 1
            #print ("NOT MY FAULT too")

            # Step 4: Generate the list L of [s',f(s')] pairs where the s' are the successors
            # of s and their f values are computed using f(s') = g(s')+h(s').

            gs = self.g[S]  # Save the cost of getting to S in a variable.
            L = []

            for op in self.Problem.OPERATORS:
                if op.is_applicable(S):
                    new_state = op.apply(S)
                    fs = gs +S.edge_distance(new_state)+ self.h(new_state)
                    L.append((new_state, fs))
                    if_update = True

                    # If there is already a pair [s', q] on CLOSED (for any value q):
                    #   if f(s') > q, then remove [s’,f(s')] from L.
                    #   If f(s') <= q, then remove [s',q] from CLOSED.

                    for (s1, q) in self.CLOSED:
                        if new_state == s1:
                            if fs > q:
                                L.remove((new_state, fs))
                                if_update = False
                            else:
                                self.CLOSED.remove((s1, q))


                    # Else if there is already a pair [s', q] on OPEN (for any value q):
                    # if f(s') > q, then remove [s’,f(s')] from L.
                    # If f(s') <= q, then remove [s',q] from OPEN.

                    if new_state in self.OPEN:
                        if fs > self.OPEN[new_state]:
                            # del L[new_state]
                            L.remove((new_state, fs))
                            if_update = False
                        else:
                            del self.OPEN[new_state]

                    if if_update:
                        edge_cost = S.edge_distance(new_state)
                        new_g = gs + edge_cost
                        self.BACKLINKS[new_state] = S
                        self.g[new_state] = new_g

            # STEP 5. Insert all members of L onto OPEN.
            for (s, q) in L:
                self.OPEN.insert(s, q)
                    
            print("After")
            txt = "OPEN: "
            for (s,q) in self.OPEN.q:
                txt += "(" + str(s) + ", " + str(q) + "), "
            print ("\n" +txt)
            
            txt = "L: "
            for (s,q) in L:
                txt += "(" + str(s) + ", " + str(q) + "), "
            print (txt)
            txt = "CLOSED: "
            for (s,q) in self.CLOSED:
                txt += "(" + str(s) + ", " + str(q) + "), "
            print (txt)

                
        print_state_queue("OPEN", self.OPEN)
        
        # STEP 6. Go to Step 2.
        return None  # No more states on OPEN, and no goal reached.

    def backtrace(self, S):
        path = []
        while S:
            path.append(S)
            S = self.BACKLINKS[S]
        path.reverse()
        print("Solution path: ")
        for s in path:
            print(s)
        return path


def print_state_queue(name, q):
    """
    Prints the states in queue q
    """
    print(f"{name} is now: ", end='')
    print(str(q))


def report(opn, closed, count):
    """
    Reports the current statistics:
    Length of open list
    Length of closed list
    Number of states expanded
    """
    print(f"len(OPEN)= {len(opn)}", end='; ')
    print(f"len(CLOSED)= {len(closed)}", end='; ')
    print(f"COUNT = {count}")


if __name__ == '__main__':
    if sys.argv == [''] or len(sys.argv) < 2:
        Problem = "FranceWithDXHeuristic"
    else:
        Problem = sys.argv[1]
    aStar = AStar(Problem)
    aStar.runAStar()
