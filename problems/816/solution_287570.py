def maiores(l,n):
    l.append(n)
    l.sort()
    i = l.index(n)
    return l[i+1:]