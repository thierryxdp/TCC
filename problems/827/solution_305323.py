def qtd_divisores(n):
    '''A função define quantos números é divisível por n ou quantos números
    n tem de divisores'''
    
    soma_n = []
    
    for x in range(1,n+1):
        if ((n+1) % x) == 0:
            list.append = (soma_n, x)
    return soma_n