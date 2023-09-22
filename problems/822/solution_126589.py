def repetidos(numeros):
    """
    
    """
    i=1
    contador=0
    while i<len(numeros):
    	if numeros[i]==numeros[i-1]:
            i+=1
            contador+=1
        else:
            i+=1
	return contador