def repetidos(lista):
    i=0
    c=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            c+=1
        i+=1
	return c