def filtraMultiplos(l,n):
    """Retorna uma lista contendo todos os elementos da listas originais que forem divisiveis por n.
    list,int->list"""
    lp = []
    i = 0
    while i <= len(l):
        if (l[i])%n == 0:
        	lp.append(l[i])
        i += 1
	return lp