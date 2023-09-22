def maiores(lista, n):
	lista.append(n)
	lista.sort()
	return lista[lista.index(n)+lista.count(n):]

def acima_da_media(notas):
    notas.sort()
    return maiores(notas,4)