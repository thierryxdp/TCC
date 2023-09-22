def par(x):
    if x%2==0:
        return True
    else:
        return False

def filtra_pares(tupla):
    return tuple(filter(par,( tupla[0],tupla[1],tupla[2],tupla[3])))