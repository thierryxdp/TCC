def filtra_impares(t):
    ret=()
    
    if par(t[0]):
        ret = ret + (t[0],)
    if par(t[1]):
        ret = ret + (t[1],)
    if par(t[2]):
        ret = ret + (t[2],)
    if par(t[3]):
        ret = ret + (t[3],)
        return ret

def par(Num):
    return Num%2==0