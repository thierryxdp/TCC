def maiores(l, n):
    ''
    l= l + [n]
    list.sort(l)
    p=l.index(n)
    return l[p:]