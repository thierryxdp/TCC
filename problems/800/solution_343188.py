def total(lista,produtos):
    '''
    Funçao que recebe uma lista de compras e um dicionario com produtos 
    no mercado e seus preços calcula o valor da lista de compras
    list, dict -> float
    '''
	pro=list(dict.keys(produtos))
    t=0
    for i in lista:
        for j in pro:
            if i == j:
                t=t+produtos[j]
	return round(t,2)