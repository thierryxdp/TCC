def primo(n):
    ''' Funcao que, dado um numero inteiro positivo, retorna se ele e ou nao 
    um numero primo (True para sim e False para nao);
    
    int -> bool '''
    
    divisores = []
    
    for numero in range(1,n+1):
        
        if (n % numero == 0):
            
            divisores = divisores + [numero]
        
    return len(divisores) <= 2