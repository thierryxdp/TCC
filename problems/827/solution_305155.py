def qtd_divisores(n):
    '''A função calculará a quantidade de divisores que um numero (n) possui
    dados de entrada -> int
    dados de saída -> int'''
    
    divisores = [2,3,4,5,6,7,8,9]
    c = 2 #todo numero é divisivel por 1 e por ele mesmo.
    
    if n < 0:
        return 0
    
    for i in divisores:
        if n % i == 0:
            c += +1
    return c