def soma_h(N):
    '''
    	sendo H = 1 + 1/2 + 1/3 + ... + 1/N
        A Função determina o valor H, dado o valor de N.
        int -> int
    '''
    H = 1
    for x in range(2,N):
        H += 1/x
    round(H,2)
    return H