def par(Num):
    return Num%2==0

def filtra_impares(t):
    impares=()
    
    if par(t[0]):
        impares = impares + (t[0],)
    if par(t[1]):
        impares = impares + (t[1],)
    if par(t[2]):
        impares = impares + (t[2],)
    if par(t[3]):
        impares = impares + (t[3],)
        return impares