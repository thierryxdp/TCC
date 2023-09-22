def qtd_divisores(num):
    """
    int->int"""
    
    divisores = 1
    i = 1
    for i in range (num):
        
        if i%num == 0 :
            divisores +=1
            
	return divisores