def maiores(l,n):
    l.append(n)
    l.sort()
    return l[l.index(n)+l.count(n):]