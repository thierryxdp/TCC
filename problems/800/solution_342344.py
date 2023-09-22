def total(compras, produtos):
    valor_compras = 0
    for contador in range(len(compras)):
        if compras[contador] in produtos:
            valor_compras = valor_compras + produtos[compras[contador]]
	return round(valor_compras, 1)