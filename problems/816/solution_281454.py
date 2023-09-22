def maiores(ls, n):
    cp = ls[:] + [n] # tenho certeza que n in cp
    list.sort(cp) # cp totalmente ordenada
    pos = cp.index(n)
    return cp[pos + 1 : ]