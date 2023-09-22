def inclui(l, n):
    list.insert(l, 1, n)
    return l
def ordena(l, n):
    list.sort(lnclui(l, n))
    return l
def maiores(l, n):
    for t in l:
        list.remove(ordena(l, n), t)
        t <= n
    return l