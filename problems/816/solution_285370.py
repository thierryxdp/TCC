def maiores(l, n):
    ''
    l= l + [n]
    list.sort(l)
    p=l.index(n)
    l=l[p:] 
    l.pop(0)
    return l