def total(compras, precos):
    '''Função que dados uma lista e um dicionário, 
    retorna a soma dos valores dos produtos da lista
    list,dict - > int'''  
    preco = 0
    for i in compras:
        if i in precos:
            preco += precos[i]
	return round(preco, 2)