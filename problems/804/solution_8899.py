def filtra_pares(tupla): tuple -> tuple
    """ Filtra os pares da tupla inserida"""
    nova_tupla= ()
    if tupla[0] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[0],)
    if tupla[1] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[1],)
    if tupla[2] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[2],)
    if tupla[3] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[3],)