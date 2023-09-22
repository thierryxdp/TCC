def filtra_pares(tupla):
    pares=()
    if tupla[0]%2 == 0:
        pares = pares + (tupla[0],)
    elif tupla[1]%2 == 0:
        pares = pares + (tupla[1],)
    elif tupla[2]%2 == 0:
        pares = (tupla[2],)
    elif tupla[3]%2 == 0:
        pares = (tupla[3],)
    return pares