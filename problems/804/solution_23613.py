def filtra_pares(tupla):
    " retorna uma nova tupla com apenas os "
    "elementos pares da tupla original"
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