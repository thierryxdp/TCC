def maiores(lista,n):
    '''recebe uma lista de números inteiros e um número
    inteiro n, retornando outra lista contendo todos os
    números da lista original maiores que n, em ordem
    crescente.
    [int],int->[int]'''
    list.sort(lista)
    posi = list.index(lista,n)
    return lista[posi:]