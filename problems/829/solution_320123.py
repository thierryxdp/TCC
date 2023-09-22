def soma_h (N):
    '''
    Retorna o valor de H com N.
    int -> float
    '''
    H = 0
    for n in range(1,N +1):
        H = H + (1/n)
    return round(H,2)