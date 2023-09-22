def fatorial(n):
    '''A função retornará o fatorial do número inserido.
    Dados de entrada -> int
    Dados de saída -> int'''
    
    i = 1
    fatorial = n
    
    while n-i != 0:
        fatorial = fatorial * (n-i)
        i = i +1
        
    return fatorial