def total(lista_compras,dic_produtos):
	""" Recebe uma lista de compras e um dicionário com produtos e preços de uma loja e retorna o valor da copra; list, dict-> float."""
    total_compra=0
	for produto in lista_compras:
		if produto in dic_produtos:
            subtotal=dict.get(dic_produtos,[produto])
			total_compra+=subtotak
	return round(total_compra,2)