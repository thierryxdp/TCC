def total(lista,preco):
    """Esta função calcula o valor total do preço de todos os produtos de uma loja
	list,dict -> float """
	soma = 0
	i = 0
	for item  in lista:
		if lista[i] in preco:
			soma += preco[lista[i]]
			i += 1
	return round(soma,2)