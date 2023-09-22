def maiores(lista_int, n):
    '''
    dada uma lista de números inteiros e um número
    inteiro n, retorna uma lista com todos os
    valores de lista_int maiores que n
    
    lista, int -> lista
    '''
    
    lista_int.insert(n, 0)
    lista_int.sort()
    lista = lista_int[(lista_int.index(n))+1:]
    return lista