def maiores(l,n):
    l.append(n)
    l.sort()
    a = l.index(n)
    b = l[a+1:]
    return b