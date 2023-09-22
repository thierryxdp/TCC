def maiores(lista, n):
    lista_nova = []
    for e in lista:
        if e >= n:
            lista_nova.append(e)
	return lista_nova