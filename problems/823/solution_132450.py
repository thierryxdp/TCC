def faltante(lista):
    i=0
    while i<len(lista):
        if lista[i] in range(len(lista)+2)[1:]:
    	i+=1
    	return lista[i]