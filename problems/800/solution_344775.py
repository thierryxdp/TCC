def total(lista, produtos):
    soma = 0
    for c in lista:
        if c in produtos.keys():
            soma+=produtos[c]
            soma = round(soma,2)
	return soma