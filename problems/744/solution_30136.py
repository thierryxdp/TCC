def insertChar(s):
    meio = len (s)/2
    meio = int(round(meio))
    mystering = '#'+s[:meio] + s[meio:] +'#'
    return mystering