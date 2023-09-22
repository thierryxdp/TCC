def faltante(lista):
    '''função que verifica e retorna qual número faltante em uma lista de números inteiros de tamanho não especificado; list -> int'''
    
    lista.sort()
    i = 0
    while i < len(lista):
        if lista[i] == lista[i]+1:
            i = i+1
    return lista[i]+1