def total(lista, preco):
	'''Função retorna os preços de uma compra baseado nos preços de cada produto
       list dic --> int'''
    precos = []
    for i in lista:
        if i in dict.keys(preco):
            precos.append(preco[i])
    return round(sum(precos),2)