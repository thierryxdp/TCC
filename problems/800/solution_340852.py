def total(lista, dic):
    soma = 0
    for itens in lista:
        if itens in dic[preco]:
            soma += preco
	return soma