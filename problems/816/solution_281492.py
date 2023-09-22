def maiores(lista_int, n):
    '''Dada uma lista de números inteiros e um inteiro n,
    retorna outra lista contendo todos os números da lista
    original maiores que n ordenados na ordem crescente
    list, int -> list'''
    lista_int = lista_int + [n]
    list.sort(lista_int)
    pos_n = list.index(lista_int, n)
    lista_int = lista_int[pos_n + 1:]
    return lista_int