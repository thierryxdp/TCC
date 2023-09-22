def fatorial(n):
    '''A função retornará o fatorial do número inserido.
    Dados de entrada -> int
    Dados de saída -> int'''
    
    i = 1
    fatorial = 1
    
    while n-i != 0:
        fatorial =fatorial * n * (n-i)
        i = i +1
        
    return fatorial