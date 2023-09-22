def fatorial(n):
    """recebe um número inteiro n e retorna o fatorial desse númro
    int->int"""
    if n==0 or n==1: 
        return 1
    else: 
        x = 1
        while(n > 1): 
            n=n-1
            x=x*n 
        return x