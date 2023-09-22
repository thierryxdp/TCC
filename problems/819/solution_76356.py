def filtraMultiplos(lista,n):
    '''função que dados uma lista com números inteiros e um número n, retorna os
       elementos desta lista que forem divisíveis por n. lista, int -> lista'''
    pos = 0
    lista_n = []
    while pos < len(lista):
        if (lista[pos] % n == 0):
            list.append(lista_n, lista[pos])
    pos = pos + 1
    return lista_n