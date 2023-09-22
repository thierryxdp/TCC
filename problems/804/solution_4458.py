def filtra_pares (x,y,z,w):

    pares=[]

    for n in (x,y,z,w):
        if n%2 == 0:
            pares.append(n)

    return tuple(pares)