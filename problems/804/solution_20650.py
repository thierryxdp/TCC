def par(n):
    if n%2==0:
        return True
    else:
        return False

def filtra_pares(t):
    ret= ()
    if par(t[0]):
        ret=ret+(t[0], )
    if par(t[1]):
        ret=ret+(t[1], )
    if par(t[2]):
        ret=ret+(t[2], )
    if par(t[3]):
        ret=ret+(t[3], )
    return ret