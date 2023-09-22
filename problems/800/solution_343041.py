def total(lista,dicio):
    '''
    Funçao que recebe uma lista e um dicionario e
    retorna o valor da lista de compras
    list, dicio -> float
    '''
    valorfinal=0
    a=list(dict.keys(dicio))
    for i in range(len(lista)):
        for j in range(len(a)):
            if lista[i] == a[j]:                
    			for x in range(len(a):
            		valor=dicio[a[x]]	
            		valorfinal= valorfinal+valor
    				x=x+1
			j=j+1
		i=i+1                     
    return valorfinal