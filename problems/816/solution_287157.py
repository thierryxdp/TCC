def maiores(lista1,n):
    '''Retorna outra lista que contenha todos os números da lista
    original maiores que n,ordenados em ordem crescente.
    list -> list'''
    lista2 = list.copy(lista1)
    list.sort(lista2)
    lista2 = lista2 > n
    return lista2