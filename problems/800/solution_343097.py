def total(lista,preco):
    """."""
	soma = 0
	i = 0
	for item  in lista:
		if lista[i] in precos:
			soma += precos[lista[i]]
			i += 1
	return round(soma,2)