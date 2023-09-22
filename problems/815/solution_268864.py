def insere(lista_numero,n):
	if n in lista_numero:
		lista_numero.sort()
		return lista_numero
	elif n not in lista_numero:
		liss = lista_numero + n
		liss.sort()
		return liss