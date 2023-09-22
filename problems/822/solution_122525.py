def repetidos(lista):
    i=0
    n=0
    while i<len(lista)-1:
        if lista[i+1]==lista[i]:
        	n=n+1
		i=i+1
    return n