def maiores(lista, n):
    '''Retorna uma lista com os valores maiores que um inteiro escolhido. list, int -> list'''
    lista1 = lista + [n]
    lista1.sort()
    y = lista1.index(n)
    del(lista1[0:y+1])
    return lista1