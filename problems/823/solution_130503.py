def faltante(lista):
    
    lista.sort()
    num = lista[0]
    faltante=1
    while i < len(lista):
    	if lista[i] != num:
            faltante = num   
		i+=1
		num+=1
	return faltante