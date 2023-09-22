def soma_h(N):
    ''' retorna a soma de 1 + 1/2 + 1/3 ... 1/N.
    int -> float'''

    H = 0
    
    for i in range(1,N+1):
        H = H + 1/i
    return round(H, 2)