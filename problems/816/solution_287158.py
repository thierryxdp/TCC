def maiores(l,n):
    l.append(n)
    list.sort(l)
    nn = l.index(n)
    lista1 = l[nn::]
	return lista1