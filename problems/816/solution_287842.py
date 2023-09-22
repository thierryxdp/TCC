def maiores(l, n):
    l.append(n)
    l.sort()
    return l[l.index(n) + 1:]