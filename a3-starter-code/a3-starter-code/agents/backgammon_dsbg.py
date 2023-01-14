'''
Name(s): Anthony Zhang, Sean Gao
UW netid(s):
'''

from game_engine import genmoves
import math

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        self.maxdepth = 2
        self.prune = True
        self.explored = 0
        self.cutoffs = 0
        # feel free to create more instance variables as needed.

    # TODO: return a string containing your UW NETID(s)
    # For students in partnership: UWNETID + " " + UWNETID
    def nickname(self):
        # TODO: return a string representation of your UW netid(s)
        return "seangao & anthoz3"

    # If prune==True, then your Move method should use Alpha-Beta Pruning
    # otherwise Minimax
    def useAlphaBetaPruning(self, prune=False):
        # TODO: use the prune flag to indiciate what search alg to use
        self.prune = prune
        self.explored = 0
        self.cutoffs = 0

    # Returns a tuple containing the number explored
    # states as well as the number of cutoffs.
    def statesAndCutoffsCounts(self):
        # TODO: return a tuple containig states and cutoff
        return (self.explored, self.cutoffs)

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. maxply=2 indicates that
    # our search level will go two level deep.
    def setMaxPly(self, maxply=2):
        # TODO: set the max ply
        self.maxdepth = maxply

    # If not None, it update the internal static evaluation
    # function to be func
    def useSpecialStaticEval(self, func):
        # TODO: update your staticEval function appropriately
        pass

    # Given a state and a roll of dice, it returns the best move for
    # the state.whose_move.
    # Keep in mind: a player can only pass if the player cannot move any checker with that role
    
    def initialize_move_gen_for_state(self, state, who, die1, die2):
        self.move_generator = self.GenMoveInstance.gen_moves(state, who, die1, die2)
    

    def get_all_moves_states(self, state, die1, die2):
        """Uses the mover to generate all legal moves."""
        self.initialize_move_gen_for_state(state, state.whose_move, die1, die2)
        move_list = []
        done_finding_moves = False
        any_non_pass_moves = False
        while not done_finding_moves:
            try:
                m = next(self.move_generator)    # Gets a (move, state) pair.
                # print("next returns: ",m[0]) # Prints out the move.    For debugging.
                if m[0] != 'p':
                    any_non_pass_moves = True
                    move_list.append((m[0], m[1]))    # Add the move to the list.
            except StopIteration as e:
                done_finding_moves = True
        if not any_non_pass_moves:
            move_list.append(('p', state))
        return move_list

    def move(self, state, die1=1, die2=6):
        # TODO: return a move for the current state and for the current player.
        # Hint: you can get the current player with state.whose_move
        if self.prune:
            print (self.alphaBeta(state, self.maxdepth, die1, die2, False, math.inf, -math.inf)[0])
            return self.alphaBeta(state, self.maxdepth, die1, die2, False, math.inf, -math.inf)[0]
        else:
            return self.minmax(state, self.maxdepth, die1, die2, False)[0]

    # Hint: Look at game_engine/boardState.py for a board state properties you can use.
    
    def minmax(self, state, depth, die1, die2, is_min):
        if depth == 0:
            """lst = self.get_all_moves_states(state, die1, die2)
            t = (lst[0][0], self.staticEval(lst[0][1]))
            se = t[1]
            for (m,s) in lst:
                self.explored += 1
                se_new = self.staticEval(s)
                if (se_new < se) == is_min:
                    se = se_new
                    t = (m, se_new)
            return t"""
            return(None, self.staticEval(state))
        lst = self.get_all_moves_states(state, die1, die2)
        #print("lst: " + str(lst))
        t = (lst[0][0], self.minmax(lst[0][1], depth-1, die1, die2, not is_min)[1])
        se = t[1]
        for (m,s) in lst:
            self.explored += 1
            se_new = self.minmax(s, depth-1, die1, die2, not is_min)[1]
            if (se_new < se) == is_min:
                se = se_new
                t = (m, se_new)
        return t

    def alphaBeta(self, state, depth, die1, die2, is_min, alpha, beta):
        if depth == 0:
            """if is_min:
                best = math.inf
            else:
                best = -math.inf
            lst = self.get_all_moves_states(state, die1, die2)
            t = (lst[0][0], self.staticEval(lst[0][1]))
            se = t[1]
            for (m,s) in lst:
                self.explored += 1
                se_new = self.staticEval(s)
                if (se_new < se) == is_min:
                    se = se_new
                    t = (m, se_new)
                if is_min:
                    best = min(best, se)
                    beta = min(beta, best)
                else:
                    best = max(best, se)
                    alpha = max(alpha, best)
                if beta <= alpha:
                    self.cutoffs += 1
                    print ("self.cutoffs: "+ str(self.cutoffs))
                    break
            return t"""
            return(None, self.staticEval(state))
        if is_min:
            best = math.inf
        else:
            best = -math.inf
        lst = self.get_all_moves_states(state, die1, die2)
        #print("lst: " + str(lst))
        t = (lst[0][0], self.alphaBeta(lst[0][1], depth-1, die1, die2, not is_min, alpha, beta)[1])
        se = t[1]
        for (m,s) in lst:
            self.explored += 1
            se_new = self.alphaBeta(s, depth-1, die1, die2, not is_min, alpha, beta)[1]
            t = (m, se_new)
            """if (se_new < se) == is_min:
                se = se_new
                t = (m, se_new)
            if is_min:
                best = min(best, se)
                beta = min(beta, best)
            else:
                best = max(best, se)
                alpha = max(alpha, best)
            if beta <= alpha:
                self.cutoffs += 1
                print ("self.cutoffs: "+ str(self.cutoffs))
                break"""
            if not is_min:
                if se_new >= beta:
                    self.cutoffs += 1
                    break
                alpha = max(alpha, se_new)
            else:
                if se_new <= alpha:
                    self.cutoffs += 1
                    break
                beta = min(beta, se_new)
        return t

    def staticEval(self, state):
        # TODO: return a number for the given state

        whitePipCount = 0
        redPipCount = 0
        whiteAnchorScore = 0
        redAnchorScore = 0
        whiteBlotScore = 0
        redBlotScore = 0
        whiteBarScore = 0
        redBarScore = 0
        whiteBearOffScore = len(state.white_off)
        redBearOffScore = len(state.red_off)

        for item in state.bar:
            if item == 0:
                whiteBarScore += 1
            if item == 1:
                redBarScore += 1
        # print("state.pointlist = ", state.pointLists)
        # if whiteScore ==  0 and redScore == 0:
        for spikes in state.pointLists:
            if len(spikes) == 2:
                if 1 not in spikes:
                    whiteAnchorScore += 1
                if 0 not in spikes:
                    redAnchorScore += 1
            if len(spikes) == 1:
                if spikes[0] == 0:
                    whiteBlotScore += 1
                if spikes[0] == 1:
                    redBlotScore += 1
            for piece in spikes:
                if piece == 0:  # white
                    whitePipCount += abs(state.pointLists.index(spikes) - 23) + 1
                if piece == 1:  # red
                    redPipCount += state.pointLists.index(spikes) + 1

        score1 = (redPipCount) - (whitePipCount)

        whiteScore = 0
        redScore = 0

        if(self.isLateGame(state)):
            whiteScore += 40 * whiteBearOffScore
            redScore += 40 * redBearOffScore
            whiteScore -= 20 * whiteBarScore
            redScore -= 20 * redBarScore
            # whiteScore += whiteAnchorScore
            # redScore += redAnchorScore
            # whiteScore -= whiteBlotScore
            # redScore -= redBlotScore

            """use for tunning, please ignore """
            whiteScore += 2*whiteAnchorScore
            redScore += 2*redAnchorScore
            whiteScore -= 3*whiteBlotScore
            redScore -= 3*redBlotScore
        else:
            whiteScore += 40 * whiteBearOffScore
            redScore += 40 * redBearOffScore
            whiteScore -= 20 * whiteBarScore
            redScore -= 20 * redBarScore
            # whiteScore += whiteAnchorScore
            # redScore += redAnchorScore
            # whiteScore -= whiteBlotScore
            # redScore -= redBlotScore

            """use for tunning, please ignore """
            whiteScore += 3*whiteAnchorScore
            redScore += 3*redAnchorScore
            whiteScore -= 5*whiteBlotScore
            redScore -= 5*redBlotScore

        score2 = whiteScore - redScore

        return score1 + score2

    def isLateGame(self, state):
        isLateGame = True
        for spikes in state.pointLists[0:11]:
            for piece in spikes:
                if piece == 0:
                    isLateGame = False
        for spikes in state.pointLists[12:23]:
            for piece in spikes:
                if piece == 1:
                    isLateGame = False
        return isLateGame
