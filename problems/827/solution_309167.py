def qtd_divisores(num):
    """
    int->int"""
    
    divisores = 0
    i = 1
    resto = 0
    while i <= num:
        resto = num%i
        if resto == 0 :
        	divisores = divisores + 1
    	i = i +1
    
    
    
    
    #for i in range(num):
     #   resto = i%num
      #  if resto == 0 :
       #     divisores = divisores + 1
            
	return divisores