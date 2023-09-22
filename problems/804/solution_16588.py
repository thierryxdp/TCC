def par(num):
    return num%2 == 0

def filtra_pares(x):
    pares = ()
    if par(t[0]):
        pares = pares + (t[0],)
        if par(t[1]):
            pares = pares + (t[1],)
            if par(t[2]):
                pares = pares + (t[2],)
                if par(t[3]):
                    pares = pares + (t[2],)
                    return pares