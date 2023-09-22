def total(compras,produtos):
    valor_compras = 0
    for contador in range(len(compras)):
        if compras in produtos:
            valor_compras = valor_compras + produtos["compras"]
	return valor_compras