def maiores (lista, n):
    '''recebe uma lista de numeros inteiros e um numero inteiro n, retorna uma nova lista com apenas os numeros maiores que n'''
    '''list->list'''
    listanumeros= lista
    um = list.append(lista, n)
    list.sort(lista)
    final = listanumeros
    retorno = lista [n:]
    vazia = []
    if n in lista:
        return retorno
    else:
    
    if lista [n:]>= n:
        return vazia = vazia + [n:]