'''Farmer_Fox.py

Assignment 2, in CSE 415, Autumn 2022.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in 
# the format shown.

#<METADATA>
SOLUTION_VERSION = "2.0"
PROBLEM_NAME = "Farmer，Fox, Chicken and Grain"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHER = ['A']
PROBLEM_CREATION_DATE = "13-OCT-2022"
PROBLEM_DESC = \
    '''This is the code for the assignment that implement the Farmer-Fox-Chicken-and-GRain problem.
'''
#</METADATA>

#<COMMON_DATA>
LEFT=0 # same idea for left side of creek
RIGHT=1 # etc.
#</COMMON_DATA>


#<COMMON_CODE>
class State:
    def __init__(self, d=None):
         if d==None:
             d = {'left': ['Farmer', 'Fox', 'Chicken', "Grain"],
                  'right' : [],
                  'side' : LEFT}
         self.d = d
    def __eq__(self, s2):

        for things in ["left", "right"]:
            for item in self.d[things]:
                if item not in s2.d[things]:
                    return False
        if self.d['side'] != s2.d['side']:
            return False
            # if self.d[things] != s2.d[things]: return False
        return True

    def __str__(self):
        left = str(self.d['left'])
        right = str(self.d['right'])
        side = "left"
        if self.d['side'] == 1: side = "right"
        txt = "left: " + left + "\n"
        txt += "right: " + right + "\n"
        txt += "side: " + side + "\n"
        return txt

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        news = State({})
        news.d['left'] = self.d['left']
        news.d['right'] = self.d['right']
        news.d['side'] = self.d['side']
        return news

    def can_move(self, thing):
        side = 'left'
        if self.d['side'] == 1:
            side = "right"

        depart = self.d[side]
        if thing is None:
            departAboutTo = len(depart) - 1
        else:
            departAboutTo = len(depart) - 2
        if thing != None and thing not in depart:
            return False
        if thing != "Chicken":
            if departAboutTo == 2 and "Chicken" in depart and "Fox" in depart:
                return False
            if departAboutTo == 2 and "Chicken" in depart and "Grain" in depart:
                return False
        if thing is None and departAboutTo > 1:
            if ("Chicken" in depart and "Fox" in depart) or ("Chicken" in depart and "Grain" in depart):
                return False



        return True


    def move(self, farmer, thing):
        # news = {'left':["Farmer","Fox", "Chicken", "Grain"], 'right':[], 'boat':[]}
        # thing = "Fox"
        # farmer = "Farmer"

        news = self.copy()
        # departSide = None

        if farmer in news.d['left']:
            departSide = 'left'
            arriveSide = 'right'
        if farmer in news.d['right']:
            departSide = 'right'
            arriveSide = 'left'

        # print(departSide)
        boat = ["Farmer"]
        if thing in news.d[departSide]:
            boat.append(thing)
        # print(news[departSide])
        # print(news[arriveSide])
        # print(news['boat'])

        news.d[departSide] = [news.d[departSide] for news.d[departSide] in news.d[departSide] if news.d[departSide] not in boat]
        # self.d[departSide] = [news.d[departSide] for news.d[departSide] in news.d[departSide] if news.d[departSide] not in boat]

        # for item in news.d[departSide]:
        #     if item in boat:
        #         news.d[departSide].remove(item)

        side = news.d['side']  # Where the boat is.
        news.d[arriveSide] = [*news.d[arriveSide], *boat]
        # self.d[arriveSide].extend(boat)

        news.d['side'] = 1 - side


        print(news.d[departSide])
        print(news.d[arriveSide])
        boat.clear()



        return news

def goal_test(s):
        g = s.d['right']
        goal = ["Chicken", "Farmer", "Fox", "Grain"]
        count = 0
        for item in g:
            if item in goal:
                count += 1
        return (count == 4)

def goal_message(s):
    return "Everything is transported!! Problem solved!!"

class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
INITIAL_DIC = {'left':["Farmer","Fox", "Chicken", "Grain"], 'right':[], 'side':LEFT}
CREATE_INITIAL_STATE = lambda : State(INITIAL_DIC)
#</INITIAL_STATE>

#<OPERATORS>
Ffcg_Combinations = [("Farmer", None), ("Farmer", "Fox"),("Farmer", "Chicken"), ("Farmer", "Grain")]
OPERATORS = [Operator("The farmer cross the river with " + str(thing),
                     lambda s, thing1 = thing: s.can_move(thing1),
                     lambda s, farmer1 = farmer, thing1 = thing: s.move(farmer1, thing1))
                     for (farmer, thing) in Ffcg_Combinations]
#</OPERATORS>

# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>

