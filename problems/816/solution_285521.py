def maiores(lista, n):
    '''Dada uma lista e um numero 'n', retorna
    uma outra lista contendo todos os numeros da lista
    original maiores que 'n';
    lista, int -> lista'''
    lista1 = sorted(lista[:])
    indice = lista1.index(n) + 1
    return indice