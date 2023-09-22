def qtd_divisores(n):
    '''A função define quantos números é divisível por n ou quantos números
    n tem de divisores'''
    
    soma_n = 0
    
    for x in range(1,n+1):
        if (n % x) == 0:
            soma_n = soma_n + 1
    return soma_n