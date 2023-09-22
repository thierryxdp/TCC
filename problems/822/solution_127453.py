def repetidos(lista):
    i=0
    a=0
    lista=sorted(lista)
    while i< len(lista)-1:
        if lista[i]!=lista[i+1]:
        	if list.count(lista,lista[i])!=1:	
            	a+=1 
        i+=1
        if lista[i-1]==lista[i] and i== len(lista)-1:
        	a+=1    
    return a