def maiores(ls, n):
    cp = ls[:] + [n]
    list.sort(cp)
    # cp totalmente ordenada
    if n not in cp:
        return cp
    else:
        pos = cp.index(n)
    	return cp[n : ]