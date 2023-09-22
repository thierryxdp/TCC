def par(x):
    if x%2==0:
        return True
    else:
        return False

def filtra_pares(tupla):
    pares=tuple(filter(par,tupla))
    return pares