def maiores (lista, n):
    list.sort(lista)
    if n in lista:
        valor = int(lista.index(n))
    	return lista[valor:]
    else:
        return []