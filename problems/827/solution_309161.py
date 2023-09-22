def qtd_divisores(num):
    """
    int->int"""
    
    divisores = 0
    
    for i in range(num):
        resto = i%num
       # if resto == 0 :
            divisores = divisores + 1
            
	return divisores