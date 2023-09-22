def total(lista,dicio):
    '''
    Funçao que recebe uma lista e um dicionario e
    retorna o valor da lista de compras
    list, dicio -> float
    '''
    valorfinal=0
    a=list(dict.keys(dicio))
    for i in lista:
        for j in a:
            if i == j:
            	for x in range(len(a)):
                	valor=dicio(a[x])	
            		valorfinal= valorfinal+valor
    				x=x+1
    return valorfinal