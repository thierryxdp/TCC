def par(num):
    return num%2 == 0

def filtra_pares(x):
    pares = ()
    if par(x[0]):
        pares = pares + (x[0],)
        if par(x[1]):
            pares = pares + (x[1],)
            if par(x[2]):
                pares = pares + (x[2],)
                if par(x[3]):
                    pares = pares + (x[2],)
                    return pares