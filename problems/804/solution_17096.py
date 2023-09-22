def filtra_pares (tupla):
    filtro  = ()
    if tupla[0] % 2 == 0:
        filtro += (tupla[0],) 
        if tupla[1] % 2 == 0:
        filtro += (tupla[1],)
    if tupla[2] % 2 == 0:
        filtro += (tupla[2],)
    if tupla[3] % 2 == 0:
        filtro += (tupla[3],)
    return filtro