def maiores(ls, n):
    cp = ls[:] + [n] # tenho certeza que n in cp
    list.sort(cp) # cp totalmente ordenada
    pri = list.index(cp, n) # primeira occorrência de n
    ult = list.count(cp, n)
    return cp[pri + ult : ]