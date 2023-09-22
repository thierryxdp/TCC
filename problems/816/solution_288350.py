def maiores(l, n):
    '''Função recebe uma lista de números inteiros e um
    valor n e retorna uma lista com todos os números
    maiores que o determinado número informado.
    list, int -> list'''
    l.insert(-1, n)
    l.sort()
    l.reverse()
    x = l.index(n)
    y = l[0:x]
    y.reverse()
    return y