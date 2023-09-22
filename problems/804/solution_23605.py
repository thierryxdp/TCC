def filtra_pares(tupla):
    Pares = ()
    if tupla[0]%2 == 0:
        Pares = (tupla[0],)
    if tupla[1]%2 == 0:
        Pares = Pares + (tupla[1],)
    if tupla[2]%2 == 0:
        Pares = Pares + (tupla[2],)
    if tupla[3]%2 == 0:
        Pares = Pares + (tupla[3],)
    return Pares