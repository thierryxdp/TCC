def faltante(lista):
	list.sort(lista)
    contador = 0
    anterior = lista[contador]
    proximo = lista[contador + 1]
    if len(lista) == 1 and lista[0] != 1:
        return lista[0] - 1
    elif  len(lista) == 1 and lista == 1:
        return lista[0] + 1
    elif len(lista) > 1:
        while contador < len(lista) and proximo == anterior + 1:
        	contador = contador + 1
        	anterior = lista[contador]
        	proximo = lista[contador + 1]
        return anterior + 1
    else:
        return lista[-1] + 1