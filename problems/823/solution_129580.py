def faltante(lista):
    '''função que verifica e retorna qual número faltante em uma lista de números inteiros de tamanho não especificado; list -> int'''
    
    lista.sort()
    i = 0
    faltante = 0
    if 1 not in lista:
        return 1
    while i+1 < len(lista):
        if lista[i]+1 != lista[i+1]:
            return lista[i]+1
        i = i+1
    return lista[-1]+1