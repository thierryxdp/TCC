def maiores(l, n):
    '''Retorna uma lista com os números maiores que n.
    list, int -> list'''
    list.append(l, n)
    list.sort(l)
    i = list.index(l, n) + list.count(l, n)
    return l[i:]