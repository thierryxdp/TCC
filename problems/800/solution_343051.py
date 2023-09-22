def total(lista,dicio):
    '''
    Funçao que recebe uma lista e um dicionario e
    retorna o valor da lista de compras
    list, dicio -> float
    '''
    valorf=0
    a=list(dict.keys(dicio))
    for i in range(len(lista)):
        for j in range(len(a)):
            if lista[i] == a[j]:                
                valor=dicio[a[j]]
           	    valorf= valorf+valor	
			j=j+1
		i=i+1                     
    return x