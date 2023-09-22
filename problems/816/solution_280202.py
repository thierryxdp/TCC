def maiores(lista_int,n):
    '''retorna uma lista com os números maiores que n
    list -> list'''
    list.append(lista_int,n)
    list.sort(lista_int)
    po = list.index(lista_int,n)
    del lista_int[0:po+1]
    return lista_int