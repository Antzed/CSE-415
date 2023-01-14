'''
Name(s):
UW netid(s):
'''

from game_engine import genmoves
import math

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        self.maxdepth = 2
        self.explored = 0
        self.step = 0
        self.dic = {}
        self.staticE = {}
        self.tryout = False
        self.howmanyyet = 0
        self.total = "N"
        # feel free to create more instance variables as needed.

    # TODO: return a string containing your UW NETID(s)
    # For students in partnership: UWNETID + " " + UWNETID
    def nickname(self):
        # TODO: return a string representation of your UW netid(s)
        return "seangao & anthoz3"

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. Count the chance nodes
    # as a ply too!
    def setMaxPly(self, maxply=2):
        # TODO: set the max ply
        self.maxdepth = maxply

    # If not None, it update the internal static evaluation
    # function to be func
    def useSpecialStaticEval(self, func):
        # TODO: update your staticEval function appropriately
        pass

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
                    if m[1] not in self.staticE.keys():
                        self.staticE[m[1]] = self.staticEval(m[1])
            except StopIteration as e:
                done_finding_moves = True
        if not any_non_pass_moves:
            move_list.append(('p', state))
            if state not in self.staticE.keys():
                        self.staticE[state] = self.staticEval(state)
        return move_list

    # Given a state and a roll of dice, it returns the best move for
    # the state.whose_move
    # Keep in mind: a player can only pass if the player cannot move any checker with that role
    def move(self, state, die1, die2):
        # TODO: return a move for the current state and for the current player.
        # Hint: you can get the current player with state.whose_move
        lst = self.get_all_moves_states(state, die1, die2)
        t = (lst[0][0], -math.inf)
        self.step += 1
        print ("playing step " + str(self.step))
        self.howmanyyet = 0
        self.total = str(len(lst))
        for (m,s) in lst:
            exp = self.expminmax(s, self.maxdepth, False)
            self.howmanyyet += 1 
            if exp > t[1]:
                t = (m, exp)
            print ("reaching "+ str(self.howmanyyet) + "/" + self.total)
        print (t[0])
        return t[0]

    

    def expminmax(self, state, depth, is_min):
        if depth == 1:
            indicnoindex = False
            if state in self.dic.keys():
                if depth in (self.dic[state]).keys():
                    return (self.dic[state])[depth]
                else:
                    indicnoindex = True

            eachchoice = 0
            for i in [1, 2, 3, 4, 5, 6]:
                for j in [1, 2, 3, 4, 5, 6]:
                    if i < j:
                        lst = self.get_all_moves_states(state, i, j)
                        t = self.staticE[lst[0][1]]
                        for (m,s) in lst:
                            se = self.staticE[s]
                            if (se < t) == is_min:
                                t = se
                        eachchoice += 2 * t
                    if i == j:
                        lst = self.get_all_moves_states(state, i, j)
                        t = self.staticE[lst[0][1]]
                        for (m,s) in lst:
                            se = self.staticE[s]
                            if (se < t) == is_min:
                                t = se
                        eachchoice += t
            exp = eachchoice / 36
            #print ("exp: " + str(exp))
            #print ("reached the end")
            if indicnoindex:
                (self.dic[state])[depth] = exp
            else:
                self.dic[state]={depth:exp}
            return exp
            ###return self.staticE[state]
        
        indicnoindex = False
        if state in self.dic.keys():
            if depth in (self.dic[state]).keys():
                return (self.dic[state])[depth]
            else:
                indicnoindex = True
        eachchoice = 0
        for i in [1, 2, 3, 4, 5, 6]:
            for j in [1, 2, 3, 4, 5, 6]:
                if (i < j) or (i == j):
                    lst = self.get_all_moves_states(state, i, j)
                    t = self.expminmax(lst[0][1], depth-1, not is_min)
                    for (m,s) in lst:
                        se = self.expminmax(s, depth-1, not is_min)
                        if (se < t) == is_min:
                            t = se
                    if i < j:
                        eachchoice += 2 * t
                    else:
                        eachchoice += t
                    print ("step " + str(self.step) + " "+str(self.howmanyyet) + "/" + self.total+" and doing (" + str(i) + ", " + str(j) + ")")
        exp = eachchoice / 36
        #print ("exp: " + str(exp))
        if indicnoindex:
            (self.dic[state])[depth] = exp
        else:
            self.dic[state]={depth:exp}
        return exp

    # Hint: Look at game_engine/boardState.py for a board state properties you can use.
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

        if (self.isLateGame(state)):
            whiteScore += 20 * whiteBearOffScore
            redScore += 20 * redBearOffScore
            whiteScore -= 40 * whiteBarScore
            redScore -= 40 * redBarScore
            whiteScore += whiteAnchorScore
            redScore += redAnchorScore
            whiteScore -= whiteBlotScore
            redScore -= redBlotScore
        else:
            whiteScore += 10 * whiteBearOffScore
            redScore += 10 * redBearOffScore
            whiteScore -= 20 * whiteBarScore
            redScore -= 20 * redBarScore
            whiteScore += whiteAnchorScore
            redScore += redAnchorScore
            whiteScore -= whiteBlotScore
            redScore -= redBlotScore

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