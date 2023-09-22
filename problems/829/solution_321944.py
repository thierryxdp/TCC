def soma_h(n):
    ''''''
    
    H = 0
    
    for indice in range(1, n+1):
        H += (1/indice)
    return round(H, 2)