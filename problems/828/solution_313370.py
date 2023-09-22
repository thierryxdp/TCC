def primo(n):
    """Dado o numero de entrada, verifica se ele é primo;
    int -> bool"""
    
    divisor = 0
    
    for i in range(1,n+1):
        if n%i == 0:
            divisor += 1
           
    if divisor == 2:
        return True
    
    else:
        return False