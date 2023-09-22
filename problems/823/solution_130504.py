def faltante(lista):
    
    lista.sort()
    num = lista[0]
    faltante=1
    
    i=0
    while i < len(lista):
    	if lista[i] != num:
            return num   
		i+=1
		num+=1
        
    if faltante in lista:
        return len(lista)+1
    
	return faltante