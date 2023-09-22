def total(compras, produtos):
	soma = 0
	for produto in compras:
		if produto in produtos:
			soma += produtos[produto]
	return soma