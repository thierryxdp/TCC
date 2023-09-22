def filtraMultiplos (lista,n):
    '''Função que filtra os multiplos de um numero n .
    list,int->list
    '''
    i=0
    divisiveis=[]
    while i<len(lista):
        if lista[i]%n==0:
            divisiveis.append(lista[i])
    	i+=1
	return divisiveis