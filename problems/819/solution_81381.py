def filtraMultiplos (lista,n):
    '''
    list,int->list
    '''
    i=0
    divisiveis=[]
    while 1<len(lista):
        if lista[i]%n==0:
            divisiveis.append(lista[i])
    	i+=1
	return divisiveis