def filtra_pares(tupla):
    """ A função retorna uma nova tupla contendo apenas os elementos
    pares. tupla--->tupla"""
    
    nova_tupla = tuple()
    if (tupla[0]%2) == 0:
        nova_tupla = nova_tupla + (tupla[0],)
    if (tupla[1]%2) == 0:
        nova_tupla = nova_tupla + (tupla[1],)
    if (tupla[2]%2) == 0:
        nova_tupla = nova_tupla + (tupla[2],)
    if (tupla[3]%2) == 0:
        nova_tupla = nova_tupla + (tupla[3],)
    return nova_tupla