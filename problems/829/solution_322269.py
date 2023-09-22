def soma_h (N):
    '''dado N, calcula e retorna o valor de H com N termos.
       : int -> float 
    '''
    H = 1
    for elem in range(2,N+1):
        H = H + (1/elem)
    return round (H,2)