def maiores(l, n):
    list.sort(l)
    a = []
    for i in l:
        if i > n:
            list.append(l, i)
    return l