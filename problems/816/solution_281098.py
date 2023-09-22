def maiores(l, n):
    list.sort(l)
    if l[0] > n:
        return l
    else:
        return []