def total(lista, preco):
'''Função calcula o preço de uma compra de acordo com os preços de cada prduto
   list dic --> int'''
	precos = []
    for i in lista:
        if i in dict.keys(preco):
            preco.append(preco[i])
    return round(sum(precos),2)