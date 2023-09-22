def filtra_pares(tupla):
    '''Esta funcao retorna os numeros pares de uma tupla com quatro elementos inteiros, na mesma ordem em que se encontravam.'''
    '''tuple --> tuple'''
    nova_tupla = tuple()
    if tupla[0] % 2 == 0:
        nova_tupla == nova_tupla + (tupla[0],)
    if tupla[1] % 2 == 0:
        nova_tupla == nova_tupla + (tupla[1],)
    if tupla[2] % 2 == 0:
        nova_tupla == nova_tupla + (tupla[2],)
    if tupla[3] % 2 == 0:
        nova_tupla == nova_tupla + (tupla[3],)
    return nova_tupla