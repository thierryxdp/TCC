def faltante(ls):
    ls.sort
    n = len(ls) + 1

    for e in range(len(ls)):
        if ls[e]-2 == ls[e-1]:
            return ls[e]-1

    if n > len(ls):
        return n