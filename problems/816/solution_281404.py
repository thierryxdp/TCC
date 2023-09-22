def maiores(lista, n):
    '''Recebe uma lista e retorna uma lista com todos os inteiros maiores que n
       list, int -> list'''
    lista.sort()
    lista[lista.index(n):]
    return lista[lista.index(n):]