def maiores(lista_int,n):
    '''
    dada uma lista de numeros inteiros e um inteiro n,
    retorna outra lista com apenas os inteiros maiores que n
    de forma ordenada(crescente)
    dados de entrada: list, int
    retorna: list
    '''
    list.append(lista_int,n)
    list.sort(lista_int)
    m = list.index(lista_int,n)
    maiores = lista_int[m+1:]
    return maiores