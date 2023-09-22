def repetidos(lista):
    i=0
    repetidos=0
    while i<len(lista):
        i=i+1
        if lista[i]==lista[i+1]:
            repetidos=repetidos+1
    	return repetidos