def filtraMultiplos(lista, n):
    '''Dada uma lista e um valor n retorna os mutiplos de n
    list, int -> list'''
    l = []
    w = 0
    while len(lista) > w:
        if lista[w] % n == 0:
            l += [lista[w]]
        w += 1
    return l