def filtraMultiplos(lista,n):
    i=0
    lista2=[]
    while i<len(lista):
        i=i+1
    	if lista[i]%n==0:
        	lista2.append(lista[i])
    return lista2