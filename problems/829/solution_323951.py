def soma_h(N):
    '''
    '''
    H = 0
    for k in range(1, N + 1):
        h = (1/k)
        H = H + h
    return round(H, 2)