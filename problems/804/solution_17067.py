def filtra_pares (tupla):
    t = () u = () v = () w = ()
    if tupla[0] % 2 == 0:
        t += (tupla[0],)
    elif tupla[1] % 2 == 0:
        u += (tupla[1],)
    elif tupla[2] % 2 == 0:
        v += (tupla[2],)
    elif tupla[3] % 2 == 0:
        w += (tupla [3],)
    return t + u + v + w