def faltante(lista):
    i=0
    while i<len(lista):
        if (range(len(lista)+2)[1:])[i] in lista:
    		i+=1
    	return (range(len(lista)+2)[1:])[i]