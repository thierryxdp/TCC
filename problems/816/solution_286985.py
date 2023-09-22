def inclui(l, n):
    list.insert(l, 1, n)
    return l
def ordena(l, n):
    list.sort(inclui(l, n))
    return l
def posicao(l, n):
    l = ordena(l, n)
    l = l[list.index(l, n):]
    return l