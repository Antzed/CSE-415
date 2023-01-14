from math import sqrt
import math
def is_multiple_of_5(n):
    if n%5 == 0:
        return True
    else:
        return False
    
    """Return True if n is a multiple of 5; False otherwise."""


def last_prime(m):
    if (m == 2):
        return 2
    while m%2 == 0 or not isPrime(m):
        m -= 1
    return m
        

def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True


def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    delta = (b*b) - (4*a*c)
    if delta > 0:
        sqrtD = math.sqrt(delta)
        positive = (-b + sqrtD) / (2 * a)
        negative = (-b - sqrtD) / (2 * a)
        return positive, negative
    else:
        return "complex"

def new_quadratic_function(a, b, c):
    def arg(x):
        return a*x*x + b*x + c
    return arg
    """Create and return a new, anonymous function (for example
    using a lambda expression) that takes one argument x and 
    returns the value of ax^2 + bx + c."""

def perfect_shuffle(even_list):
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    Perfect shuffle means splitting a list into two halves and then interleaving
    them. For example, the perfect shuffle of [0, 1, 2, 3, 4, 5, 6, 7] is
    [0, 4, 1, 5, 2, 6, 3, 7]."""
    length = len(even_list)
    middle_index = length//2
    first_half = even_list[:middle_index]
    second_half = even_list[middle_index:]
    new_list = []

    for i in range(1, length+1):
        if i%2 != 0:
            new_list.append(first_half[0])
            first_half.pop(0)
        else:
            new_list.append(second_half[0])
            second_half.pop(0)
    return new_list

def five_times_list(input_list):
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 5."""
    """
    new_list = []
    length = len(input_list)
    for i in range(length):
        processed = input_list[i]
        processed = processed * 5
        new_list.append(processed)
    return new_list"""

    newlist = [x*5 for x in input_list]

    return newlist

def triple_vowels(text):
    """Return a new version of text, with all the vowels tripled.
    For example:  "The *BIG BAD* wolf!" => "Theee "BIIIG BAAAD* wooolf!".
    For this exercise assume the vowels are
    the characters A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", 'U']
    check =  all(item in text for item in text)
    for e in text:
        if e in vowels:
            index = text.index(e)
            text = text[:index] + e + text[index:]
            text = text[:index+1] + e + text[index+1:]
            
    return text

def count_words(text):
    """Return a dictionary having the words in the text as keys,
        and the numbers of occurrences of the words as values.
        Assume a word is a substring of letters and digits and the characters
        '-', '+', *', '/', '@', '#', '%', and "'" separated by whitespace,
        newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ] { } | : ).
        Convert all the letters to lower-case before the counting."""

    textLowered = text.lower()

    str = ",.:;!?&()[]{}|:_\n\\=><`\"^~$"
    for c in textLowered:
        if c in str:
            textLowered = textLowered.replace(c, " ")

    textLoweredlist = textLowered.split()
    text2 = []
    words = {}


    for i in textLoweredlist:
        if i not in text2:
            text2.append(i)

    for i in range(0, len(text2)):
        count = textLoweredlist.count(text2[i])
        words[text2[i]] = count
    return words




class Polygon:

    def __init__(self, n_sides, lengths=None, angles=None):
        self.n_sides = n_sides
        self.angle = angles
        self.lengths = lengths


    def is_rectangle(self):
        """ returns True if the polygon is a rectangle,
        False if it is definitely not a rectangle, and None
        if the angle list is unknown (None)."""
        chk = True
        if self.angle != None:
            for item in self.angle:
                if item != 90:
                    chk = False
                    break;
        if (self.n_sides == 4 and self.lengths == None and self.angle == None) or (self.n_sides == 4 and self.angle == None):
            return None
        elif self.n_sides == 4 and chk:
            return True
        else:
            return False

    def is_rhombus(self):
        chk = True

        if self.lengths != None:
            element = self.lengths[0]
            for item in self.lengths:
                if element != item:
                    chk = False
                    break;
        acute = 0
        abtuse  = 0
        if self.angle != None:
            for item in self.angle:
                if item < 90:
                    acute += 1
                else:
                    abtuse += 1

        if self.n_sides == 4 and chk and acute == 2 and abtuse == 2:
            return True
        elif self.n_side == 4 and self.lengths == None and self.angle == None:
            return None
        else:
            return False

    def is_square(self):
        chk = True
        if self.angle != None:
            angle = self.angle[0]
            for item in self.angle:
                if angle != item:
                    chk = False
                    break;
        if self.lengths != None:
            element = self.lengths[0]
            for item in self.lengths:
                if element != item:
                    chk = False
                    break;
        if (self.n_sides == 4 and self.angle == None and self.lengths != None and chk) or (self.n_sides == 4 and self.lengths == None and self.angle != None and chk) or (self.n_sides == 4 and self.lengths == None and self.n_sides == 4 and self.angle == None):
            return None
        elif self.n_sides == 4 and chk:
            return True
        else:
            return False

    def is_regular_hexagon(self):
        chk = True
        if self.lengths != None:
            element = self.lengths[0]
            for item in self.lengths:
                if element != item:
                    chk = False
                    break;
        if self.angle != None:
            elementAngle = self.angle[0]
            for item in self.angle:
                if elementAngle != item:
                    chk = False
                    break;

        if (self.n_sides == 6 and self.lengths == None and self.angle != None and chk) or (self.n_sides == 6 and self.angle == None and self.lengths != None and chk):
            return None
        elif self.n_sides == 6 and chk:
            return True
        else:
            return False

    def is_isosceles_triangle(self):
        chk = False
        if self.lengths != None:
            if (self.lengths[0] == self.lengths[1] and self.lengths[1] != self.lengths[2]) or (self.lengths[1] == self.lengths[2] and  self.lengths[2] != self.length[0]) or (self.lengths[2] == self.lengths[0] and self.lengths[0] != self.lengths[1]):
                chk = True
            else:
                chk = False
        if self.angle != None:
            if self.angle[0] == self.angle[1] or self.angle[1] == self.angle[2] or self.angle[2] == self.angle[0]:
                chk = True
            else:
                chk = False
        if self.n_sides == 3 and self.lengths == None and self.angle == None:
            return None
        elif self.n_sides == 3 and chk:
            return True
        else:
            return False

    def is_equilateral_triangle(self):
        chk = True
        if self.angle != None:
            for item in self.angle:
                if item != 60:
                    chk = False
                    break;
        if self.lengths != None:
            element = self.lengths[0]
            for item in self.lengths:
                if element != item:
                    chk = False
                    break;

        if(self.n_sides == 3 and self.lengths == None and self.angle == None):
            return None
        elif (self.n_sides == 3 and chk):
            return True
        else:
            return False

    def is_scalene_triangle(self):
        if self.n_sides != 3:
            return False
        if self.angle != None:
            if (len(set(self.angle)) == len(self.angle)):
                return True
            else:
                return False
        if self.lengths != None:
            if (len(set(self.lengths)) == len(self.lengths)):
                return True
            else:
                return False













#my_tri = Polygon(3, lengths=[3, 4, 5])
#print(my_tri.is_rectangle()) # False
#print(my_tri.is_isosceles_triangle())  # False
#print(my_tri.is_scalene_triangle())  # True

#your_tri = Polygon(3, angles=[60, 60, 60])
#print(your_tri.is_equilateral_triangle()) # True
#print(your_tri.is_isosceles_triangle()) # True"
#your_tri.is_scalene_triangle()  # False

#my_rect = Polygon(4, angles=[90, 90, 90, 90])
#print(my_rect.is_rectangle())# True
#print(my_rect.is_square())  # None (unknown)

#your_diamond = Polygon(4, [1, 1, 1, 1], [114, 66, 114, 66])
#your_diamond.print()
"""your_diamond.is_rectangle()  # False
your_diamond.is_rhombus()  # True"""
#print(your_diamond.is_square() ) # False"""
    
