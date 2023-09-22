def fatorial(x):
    '''funcao que retorna o fatorial de um numero x int->int'''
    
    i = 1
    
    f = 1
    
    while x >= i:
        
        f*= i
        i = i + 1
    
    return f