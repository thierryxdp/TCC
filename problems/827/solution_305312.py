def qtd_divisores(n):
    '''A função define quantos números é divisível por n ou quantos números
    n tem de divisores'''
    
    soma_n = 0
    
    for x in range(n):
        if (n % x) == 0:
            soma_n = soma_n + n
    return soma_n