def soma_h(n):
    '''
    funcao que recebe um valor n e calcula o valor de h,
    onde h = 1 + 1/2 + 1/3 + 1/4 .... + 1/n
    int-> float
    '''
    
    i = 1
    h = 0
    for i in range(1,n+1):
        h = h + 1/i
        i += 1
    
    return round(h,2)