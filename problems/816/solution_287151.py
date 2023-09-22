def maiores(l,n):
    l.append(n)
    list.sort(l)
    nn = l.index(n)
    lista1 = l[n::]
	return lista1, nn