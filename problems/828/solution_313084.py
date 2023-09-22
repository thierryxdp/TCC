def qtd_divisores(n):
    '''A função calculará a quantidade de divisores que um numero (n) possui
    dados de entrada -> int
    dados de saída -> int'''
    
    c = 0 #contador
    
    if n < 0:
        return 0
    
    for i in list(range(1,n+1)):
        if n % i == 0:
            c += +1
    return c

def primo(n):
    '''A função verificará se um determinado numero (n) é primo ou não.
    Dados de entrada -> int
    Dados de saída -> booleano'''
    
    qtd_divisores = qtd_divisores(n)
    
    if qtd_divisores != 2:
        return False
    
    else:
        return True