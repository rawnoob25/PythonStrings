"""
Illustrates use of python's str.format method as well as its ljust, rjust
and zfill methods
"""

def sameLenOrNot(s,t):
    """
    Returns true if and only if strings s and t are the
    same length
    Precondition: s and t are both strings
    """
    if len(s) == len(t):
        print("{0} and {1} are the same length".format(s,t))
    else:
        print("the length of {0} is {1} while the length of {2}\
 is {3}".format(s,len(s),t,len(t)))
        
def illustrateJustification():
    """
    This function illustrates python's ljust and rjust str methods.
    The str.ljust(x:int) method right pads a string with spaces to
    achieve length x. If the length of the string on which ljust is invoked
    is greater than or equal to x, there is no padding. ljust left justifies
    a string by right-padding it with spaces.

    The str.rjust(x:int) method left pads a string with spaces to
    achieve length x. If the length of the string on which rjust is invoked
    is greater than or equal to x, there is no padding. rjust right justifies
    a string by left-padding it with spaces.
    """

    print("i".rjust(8)) #left-pads w/ 7 spaces
    print(computer.ljust(2)) #no padding takes place
    print("ul".ljust(10)) #right-pads w/ 8 spaces

def illustrateZfill():
    """
    This function illustrates python's zfill str method. str.zfill(n) left
    pads a string with zeros to achieve length n...if the length of the
    invoking string is greater than or equal to n, no padding takes place.

    """
    print("The time is "+"18".zfill(2)+" hours")
