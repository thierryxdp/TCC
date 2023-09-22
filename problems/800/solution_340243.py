def total(lista_compras:list, preco_produto:dict)->int:
    preco = 0
    for i in lista_compras:
        if i in preco_produto:
            preco += preco_produto[i]
	return preco