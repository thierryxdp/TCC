def colchao(medidas,H,L):
    '''Funcao que retorna True ou False a partir da entrada de uma lista e 2 valores do tipo int, respectivamente.'''
    
    if medidas[1] <= H and medidas[0] <= L:
        passar = True
    
    else:
    	if medidas[1] <= L and medidas[0] <= H:
        	passar = True
    
    	else:
        	passar = False
    
        
    return passar