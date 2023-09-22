def total(lista_compras,dict_produtos):
	"""Recebe uma lista de compras e um dicionario com produtos e seus preços e retorna o valor da compra; list,dict->float."""
    total_compra=0
    for produto in lista_compras:
		if produto in dict_produtos:
			subtotal=dict.get(dict_produtos,produto)
			total_compra+=subtotal
    return round(total_compra,2)