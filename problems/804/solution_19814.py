def par(n):
    if n%2==0:
        return True
    else:
        return False
def filtra_par (x,y,z,w):
    return list(filter(par,(x,y,z,w)))