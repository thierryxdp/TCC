def total(item, produtos):
    """Função que recebe uma lista de compras e um dicionario com o valor de cada item e volta com o valor total dessa lista de compra;
    list, dict -> float"""
    soma = 0
	for produto in lista:
		soma = soma + produtos[item]
	return soma