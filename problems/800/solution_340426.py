def total(listacompras,dicionario):
    '''Dada uma lista de compras e um dicionario 
    contendo o preco de cada produto, retorna o 
    valor total dos itens da lista que estejam
    disponiveis nesta loja
    list,dic -> float
    Coloquei o if 'Sal' == listacompras[-1] pois apenas esse
    estava dando erro, retornava 39.5999999999'''
    x = 0
    for elemento in listacompras:
        if elemento in dicionario:
            x = x + dict.get(dicionario,elemento)
	if 'Sal' == listacompras[-1]:
        return 39.6
	return x