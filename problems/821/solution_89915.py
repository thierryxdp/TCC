def fatorial(n):
    
    '''Função que dado um número,
    retorna o fatorial do mesmo.
    
    param n: int
    return:int'''
    
    i= 1
    n_fator=1  

    while i <= n:
        n_fator=n_fator*i 
        i=i+1

    return n_fator