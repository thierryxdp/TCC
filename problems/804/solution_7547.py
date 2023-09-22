def filtra_pares(tupla):
    """"""
    novatupla = ()
    if tupla[0] % 2  == 0:
        novatupla = novatupla + (tupla[0],)
    else:
        novatupla = novatupla
    if tupla[1] % 2 == 0:
        novatupla = novatupla + (tupla[1],)
    else: novatupla = novatupla
        
    if tupla[2] % 2 == 0:
        novatupla = novatupla + (tupla[2],)
    else:
        novatupla = novatupla
    if tupla[3] % 2 == 0:
        novatupla = novatupla + (tupla[3],)
    else:
        novatupla = novatupla
    return novatupla