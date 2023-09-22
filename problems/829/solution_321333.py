def soma_h(n):
    """ 
    	Funcao que recebe um numero n e calcula a soma H (H = 1 + 1 / 2 + 1 / 3 ... 1 / n);
		int -> float    
    """
    H = 1 
    
    for num in range(2, n + 1):
        H += num ** - 1
        
    return round(H, 2)