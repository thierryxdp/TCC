import math* 
def insertChar(s):
    meio = len (s)/2
    meio = int(math.floor(meio))
    mystring = '#'+s[:meio] + s[meio:] +'#'
    return mystring