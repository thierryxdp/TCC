def par(x):
    if x%2 == 0:
        return (x,)
    else:
        return tuple()

    
def filtra_pares(tupla):
    tuplapar= par(tupla[0])+par(tupla[1])+par(tupla[2])+par(tupla[3])
    
    return tuplapar