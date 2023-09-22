def filtraMultiplos(lista,n):
    '''retorna dado uma lista o numeros multiplos de n
    list,int->list'''
    divisiveis=[]
    i=0
	while i<len(lista):
    	if lista[i]%n==0:
        	divisiveis= divisiveis + [lista[i]]
		i=i+1
    return divisiveis