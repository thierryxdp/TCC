def filtraMultiplos(lista,n):
    divisiveis=[]
    i=0
	while indice<len(lista):
    	if lista[i]%n==0:
        	divisiveis+=lista[i]
		i=i+1
    return divisiveis