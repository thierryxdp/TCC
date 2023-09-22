def fatorial(n):
    '''retorna o resultado do calculo vetorial do numero n'''
    '''int -> int'''
    
    fat= 1
    i = n * (n -1)
    
    while n >= 1:
        
        fat = fat * n
        n = n - 1
        
    return fat