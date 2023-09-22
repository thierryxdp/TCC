def total(comprar, produtos):
    """A função calcula o valor dos itens na lista dentro do dicionario
    list + dic --> float"""
    i = 0.0
	for x in comprar:
        if x in produtos:
            i = i + dict.get(produtos, x)
	return round(i, 2)