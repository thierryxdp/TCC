def qtd_divisores(n):
    ''' Funcao calcula quantos divisores inteiros o numero dado como entrada 
    possui;
    
    int -> int '''
    
    divisor = 1
    divisores = []
    
    while divisor <= n:
        
        if (n % divisor == 0): 
            
            divisores = divisores + [divisor]
            
        divisor = divisor + 1

        
    return len(divisores)