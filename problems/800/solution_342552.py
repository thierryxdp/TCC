def total(lista_de_compras,dicionario):
	type(lista_de_compras)== list
	type(dicionario)==dict
	for lista in dicionario.keys():
		soma = lista.values()
		return sum(soma)