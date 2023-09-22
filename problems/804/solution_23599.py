def filtra_pares(tupla):
    Pares = ()
    if tupla[0]%2 == 0:
        Pares = tupla[0]
    elif tupla[1]%2 == 0:
        Pares = Pares + tupla[1]
    elif tupla[2]%2 == 0:
        Pares = Pares + tupla[2]
    elif tupla[3]%2 == 0:
        Pares = Pares + tupla[3]
    return Pares