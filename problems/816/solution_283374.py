def maiores(lista, n):
    '''funçao que recebe uma lista de numeros inteiros e retorna 
    uma nova lista com numeros interios maiores que n. list, int -- list'''
    lista1 = [x for x in lista if x > n]
    return lista1