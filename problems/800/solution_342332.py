def total(lista,dicionario):
    '''
	receve uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma loja e retorna o valor total da lista que estejam disponiveis nesta loja;
    lista, dict -> float
    '''
    a = len(lista)
    for compras in lista:
        compras = sum(dicionario[lista[0]:dicionario[lista[a])