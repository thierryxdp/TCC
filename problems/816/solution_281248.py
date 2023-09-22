def maiores (lista, n):
    '''recebe uma lista de numeros inteiros e um numero inteiro n, retorna uma nova lista com apenas os numeros maiores que n'''
    '''list->list'''
    listanumeros= lista
    um = list.append(lista, n)
    dois = list.sort(lista)
    final = listanumeros
    indice = lista [n:]
    if n in lista:
        return indice
    else:
        return []