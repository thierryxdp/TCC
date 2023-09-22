def maiores(lista1):
    '''Retorna outra lista que contenha todos os números da lista
    original maiores que n,ordenados em ordem crescente.
    list -> list'''
    lista2 = list.copy(lista1)
    list.sort(lista2)
    return lista2