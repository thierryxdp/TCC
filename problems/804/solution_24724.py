def filtra_pares(tup):
    """ Função que recebe uma tupla com 4 inteiros e retorna
    uma nova tupla contendo os elementos pares da original,
    na mesma ordem em que se encontravam;
    str -> str"""
    len(tup) == 4
    a = tup(0)
    b = tup(1)
    c = tup(2)
    d = tup(3)
    x = a, b, c, d
    pares = (x % 2 == 0)
    return pares