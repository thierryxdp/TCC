def repetidos(lista):
	"""Recebe uma lista e retorna a quantidade de vezes em que um algarismo é exatamente igual
    ao elemento anterior na ordem da lista
    assinatura: lista --> int
    """
    fim=0
    slic=lista[1:]    
    for x in lista and i in range(len(slic)):        
    	if x[i]==slic:
    		fim+=1
    return slic