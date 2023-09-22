def faltante (lista_pecas):
    '''função que dada uma lista com N-1 indica qual peça está faltando.
    list -> int'''
    list.sort(lista_pecas)
    
    if lista_pecas[0] != 1:
        return 1
    lista = list(range(lista_pecas[0],lista_pecas[-1]+1))
    if lista == lista_pecas:
        return lista_pecas[-1] + 1
    i = 0
    while i < len(lista):
        if lista[i] != lista_pecas[i]:
            return lista[i]
        i = i+1
    else:
        return i-1