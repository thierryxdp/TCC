def qtd_divisores(inteiro):
    """
    Essa função dado um numero inteiro como entrada, ira retronar
    quantos divisores tal numero tem.
    int->int
    """
    
    num_divisores = 0
    
    if inteiro < 0:
        return 0
    
    
    for e in range(1,inteiro+1):
        if inteiro % e == 0:
            num_divisores += 1
            
      
        else:
            num_divisores = num_divisores
           
        
        
    return num_divisores