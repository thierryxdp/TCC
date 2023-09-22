def qtd_divisores(n+1):
    '''A função define quantos números é divisível por n ou quantos números
    n tem de divisores'''
    
    soma_n = 0
    
    for x in range(1,n):
        if (n % x) == 0:
            soma_n = soma_n + x
    return soma_n