def maiores(l,n):
    l.append(n)
    list.sort(l)
    nn = l.index(n)
    nn = nn + 1
    lista1 = l[nn:]
	return lista1

def acima_da_media(l):
    list.sort(l)
    sum(l)
    resultado = maiores(l,5)
	return l