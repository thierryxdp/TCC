filtra_pares(tupla):
    nova_tupla = ()
    if tupla[0] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[0], )
        return nova_tupla
    elif tupla[1] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[1], )
        return nova_tupla
    elif tupla[2] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[2], )
        return nova_tupla
    elif tupla[2] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[2], )
        return nova_tupla
    elif tupla[3] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[3], )
        return nova_tupla