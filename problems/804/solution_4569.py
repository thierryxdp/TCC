def filtra_pares(x, y, z, w):
    '''Função que, dados quatro elementos inteiros como parâmetro, retorna um tupla contendo apenas os elementos pares da tupla original na mesma ordem que se encontravam; int, int, int, int -> tuple.'''
    pares = list()
    if (x % 2 == 0):
        list.insert(,pares, 0, x)
        if (y % 2 == 0):
            list.insert(pares, 1, y)
            if (z % 2 == 0):
                list.insert(pares, 2, z)
                if (w % 2 == 0):
                    list.insert(pares, 3, w)
    return tuple(pares)