def filtraMultiplos(lista,n):
    divisiveis=[]
    i=0
	while indice<len(lista):
    	if lista[indice]%n==0:
        	divisiveis+=lista[indice]
   	i=i+1
    return divisiveis