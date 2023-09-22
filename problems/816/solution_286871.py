def maiores(l, n):
    list.insert(l, 1, n)
    l = list.sort(l)
    l = list.reverse(l)

    return l