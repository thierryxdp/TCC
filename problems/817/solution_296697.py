def maiores(lista,n):
    '''recebe uma lista de números inteiros e um número
    inteiro n, retornando outra lista contendo todos os
    números da lista original maiores que n, em ordem
    crescente.
    [int],int->[int]'''
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    return lista[a+1:]

def acima_da_media(lista):
    '''recebe uma lista com notas e retorna uma lista
    com as notas acima da média. considerando media 7
    [float]->[float]'''
    return maiores(lista,7)