def faltante(lista):
    '''função que retorna o numero faltante numa sequencia '''
    '''list->int'''
    indice = 1
    lista.sort()
    while lista [ indice - 1] == indice:
        indice += 1 
        if indice > len(lista):
            return indice 
    return indice