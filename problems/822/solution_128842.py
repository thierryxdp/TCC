def repetidos(ls):
	"""Recebe uma lista e retorna a quantidade de vezes em que um algarismo é exatamente igual
    ao elemento anterior na ordem da lista
    assinatura:
    lista --> int
    testes:
    
    """
    c=0
    fat=ls[1:]    
    for i in range(len(fat)):        
    	if ls[i]==fat[i]:
    		c+=1
    return c