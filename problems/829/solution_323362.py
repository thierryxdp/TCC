def soma_h(n):
    '''
    funcao que calcula e retorna o valor H com N termos.
    int->float.
    '''
    H = 0
    for N in range (1,n+1):
        H = H + (1/N)
    return round(H,2)