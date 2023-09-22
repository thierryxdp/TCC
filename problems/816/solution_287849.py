def maiores (lista, n):
    list.sort(lista)
    if n not in lista:
        if n > int(lista[-1]):
            return lista
        else:
            return []
    else:
        valor = int(lista.index(n))
    	return lista[valor:]