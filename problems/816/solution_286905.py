def incluir(l, n):
    list.insert(l, 1, n)
    return l
def maiores(l,n):
    f = []
    list.sort(incluir(l, n))
    return l[n-1:]