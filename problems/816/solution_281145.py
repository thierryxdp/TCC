def maiores(lista_int, n):
    '''
    dada uma lista de números inteiros e um número
    inteiro n, retorna uma lista com todos os
    valores de lista_int maiores que n
    
    lista, int -> lista
    '''
    
    lista_int.insert(0, n)
    lista_int.sort()
    x = lista_int.index(n)
    lista = lista_int[x+1:]
    return lista