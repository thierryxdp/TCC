def incluir(l, n):
    list.insert(l, 1, n)
    return l
def maiores(l,n):
    f = []
    list.sort(incluir(l, n))
    for e in l:
        if e < n:
            del e
    return l