def qtd_divisores(num):
    """
    int->int"""
    
    divisores = 0
    
    for i in range(num):
        
        if i == 0:
            i += 1
        
        if num%i == 0 :
            divisores = divisores + 1
            
	return divisores