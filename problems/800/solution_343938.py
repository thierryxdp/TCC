def total(ls,d):
    """retorna o valor que sera gasto com uma lista
    de compras
    list,dict->int
    """
    contador = 0
	total = 0
	for elementos in ls:
		if ls[contador] in d:
			total += d[ls[contador]]
			contador += 1
	return round(total, 2)