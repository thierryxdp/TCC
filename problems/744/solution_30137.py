def insertChar(s):
    meio = len (s)/2
    meio = int(round(meio))
    mystring = '#'+s[:meio] + s[meio:] +'#'
    return mystring