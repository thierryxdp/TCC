def fatorial(n):
    '''Função que recebe um número e calcula o fatorial 
    desse mesmo número.
    int -> int'''
    
    i = 1
    n_fat = 1
    
    while i <= n:
        n_fat = n_fat*i
        i = i + 1
        
    return n_fat