def maiores(lista_numeros,n):
	if n in lista_numeros:
        list.sort(list_numeros)
        lista = lista[list.index(lista_numeros,n)+1:]
        return lista
    else:
		lista_numeros.insert(-1,n)
        list.sort(lista_numeros)
        lista = lista_numeros[list.index(lista_numeros,n)+1:]