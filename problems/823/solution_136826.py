def faltante (L):
    """retornar a peça faltante a partir de uma lista de peças.(list->int)"""
  
    n=1
    pecas=len(L)+1
    
    while n<pecas:
    	if n not in L:
        	return n
        if pecas not in L:
            return pecas
        else:
            n+=1