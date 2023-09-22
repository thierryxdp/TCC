def par(n):
    if n%2 == 0:
        return True
    else:
        return False
def filtra_pares(x,y,z,w):
    T = x,y,z,w
    return list(filter(par,T))