"""
Illustrates use of python's format method
"""

def sameLenOrNot(s,t):
    if len(s) == len(t):
        print("{0} and {1} are the same length".format(s,t))
    else:
        print("the length of {0} is {1} while the length of {2}\
 is {3}".format(s,len(s),t,len(t)))


        
