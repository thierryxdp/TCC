def maiores(ls, n):
    cp = ls[:]
    list.sort(cp)
    # cp totalmente ordenada
    if x not in cp:
        return cp
    else:
        pos = cp.index(n)
    	return cp[n : ]