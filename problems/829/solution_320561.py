def soma_h(N):
    H = 0
    for numero in range(1, N + 1):
        H += (1 / numero)
        
    return round(H ,2)