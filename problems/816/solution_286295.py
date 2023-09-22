def maiores(numeros, n):
    '''dada uma lista de numeros inteiros e um numero n, retorna uma lista com os numeros maiores que n;
    list[int], int -> list[int]'''
    lista = numeros + [n]
    list.sort(lista)
    list.revert(lista)
    pos_n = list.index(lista, n)
    lista = lista[:pos_n]
    list.revert(lista)
    
    return lista