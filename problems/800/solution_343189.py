def total(lista, produtos):
	'''Esta função calcula o total da lista de compras
	de acordo com os preços no dicionário
	list, dict -> float'''
	contador = 0
	total = 0
	for elementos in lista:
		if lista[contador] in produtos:
			total += produtos[lista[contador]]
			contador += 1
	return round(total, 2)