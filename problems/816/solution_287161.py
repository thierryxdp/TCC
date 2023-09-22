def maiores(l,n):
    l.append(n)
    list.sort(l)
    nn = l.index(n)
    nn = nn + 1
    lista1 = l[nn:]
	return lista1