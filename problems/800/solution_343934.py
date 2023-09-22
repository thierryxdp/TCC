def total(ls,d):
    """retorna o valor que sera gasto com uma lista
    de compras
    list,dict->int
    """
    contador = 0
	total = 0
	for elementos in lista:
		if lista[contador] in produtos:
			total += produtos[lista[contador]]
			contador += 1
	return round(total, 2)