def total(lista, dicionario):
    """Função que recebe uma lista de compras e um dicionario com o valor de cada item e volta com o valor total dessa lista de compra;
    list, dict -> float"""
    soma = 0
  	
	for produto in lista:
		soma = soma + dicionario[produto]
	return soma