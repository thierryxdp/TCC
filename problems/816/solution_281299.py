def maiores (lista, n):
    '''recebe uma lista de numeros inteiros e um numero inteiro n, retorna uma nova lista com apenas os numeros maiores que n'''
    '''list->list'''
    um = list.append(lista, n)
    list.sort(lista)
    posicao = list.index(lista, n)
    
    return lista [posicao+1:]