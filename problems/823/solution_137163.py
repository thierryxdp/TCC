def faltante(lista:list)->int:
    '''retorna qual número está faltando na lista'''
    i=0
    g = (i-1)
    while i < len(lista):
        if lista[g] != 0 and lista[g] not in lista:
            return lista[g]
    g = i-1
    i += 1
    return lista[-1]+1