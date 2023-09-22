def filtraMultiplos(lista,n):
    '''recebe como entrada uma lista e um numero n e retorna uma 
    lista com todos os numeros divisiveis por n que estavam na
    lista original; list,int->list'''
    i=0
    lista2=[]
    while i<len(lista):
    	if lista[i]%n==0:
        	lista2.append(lista[i])
    	i=i+1
    return lista2