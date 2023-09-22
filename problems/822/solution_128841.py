def repetidos(lista):
	"""Recebe uma lista e retorna a quantidade de vezes em que um algarismo é exatamente igual
    ao elemento anterior na ordem da lista
    assinatura: lista --> int
    """
    fim=0
    slic=lista[1:]    
    for i in range(len(slic)):        
    	if lista[i]==slic[i]:
    		fim+=1
    return fim