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