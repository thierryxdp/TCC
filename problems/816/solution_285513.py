def maiores(lista, n):
    '''Dada uma lista e um numero 'n', retorna
    uma outra lista contendo todos os numeros da lista
    original maiores que 'n';
    lista, int -> lista'''
    lista.sort()
    indice = int(list.index(lista[:], n) + 1)
    return lista[indice:]