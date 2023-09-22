def repetidos(lista):
    i = 0
    rep = 0
    
	for n in lista:
     	if i < len(lista)-1 : 
        	if n == lista[i+1] :
            	rep = rep + 1
            	i= i+1
        	else:
            	i = i + 1
    return rep