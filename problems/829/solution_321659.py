def soma_h(n):
    '''
    Função que soma as frações inversas de 1 até n.
    
    int -> float
    '''
    h = 0
    for a in range(1,n+1):
        h = h + 1/a
    return round(h,2)