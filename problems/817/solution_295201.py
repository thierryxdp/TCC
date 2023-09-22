def maiores(lista, n):
    '''Retorna uma lista com os valores maiores que um inteiro escolhido. list, int -> list'''
    lista1 = lista
    lista1.sort()
    y1 = sum(lista1)
    y = lista1.index
    del(lista1[0:y+1])
    return lista1