def filtramultiplos(lista, n):
    '''Dada uma lista e um valor n retorna os mutiplos de n
    list, int -> list'''
    l = []
    for i in lista:
        if i % n == 0:
            l += i
    return l