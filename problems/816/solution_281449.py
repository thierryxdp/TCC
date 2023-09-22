def maiores(ls, n):
    cp = ls[:]
    list.sort(cp)
    # cp totalmente ordenada
    pos = cp.index(n)
    return cp[n : ]