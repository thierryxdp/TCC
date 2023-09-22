def primo(inteiro):
    """
    Essa função dado um numero inteiro como entrada, ira retronar
    se o numero em questao é primo (True) ou nao(False).
    int->bool
    """
    
    num_divisores = 0
    
    if inteiro < 0:
        return False
    
    
    for e in range(1,inteiro+1):
        if inteiro % e == 0:
            num_divisores += 1
            
      
        else:
            num_divisores = num_divisores
           
        
        
    if num_divisores == 2:
        return True
    else:
        return False