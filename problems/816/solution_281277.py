def maiores (lista, n):
    '''recebe uma lista de numeros inteiros e um numero inteiro n, retorna uma nova lista com apenas os numeros maiores que n'''
    '''list->list'''
    lista_numeros= lista
    um = list.append(lista, n)
    list.sort(lista)
    indice = lista [0:n]
    indice2 = lista [n:-1]
    if n in lista:
        return indice
    else:
        return indice2