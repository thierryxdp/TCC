def soma_h(N):
    H = 1
    for numero in range(2,N+1):
        H = H + (1/numero)
    return round(H, 2)