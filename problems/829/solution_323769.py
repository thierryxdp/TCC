def soma_h(n):
    """Essa função calcula a soma de N valores
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
    int->float"""
    
    H = 0
	
    for i in range(n):
        
        H = H + (1/(n-i))
    
    
    
    
    
    
    return round(H,2)