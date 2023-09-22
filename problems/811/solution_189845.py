def colchao (medidas, H, L):
    '''Esta função define se o colchão passa pela porta ou não, dado
    sua altura e sua largura 
    list, float, float ===> bool '''
    
    if medidas [1] <= H:
        return True
    
    if madidas [2] <= L:
        return True
    
    if medidas [1] <= H:
        return True 
   
	if medidas [2] <= L:
        return True 
    
    else:
        return False