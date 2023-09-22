def soma_h (N):
    H = 0
    
    for numero in range(1,N+1):
        H = H + (H/numero)
    return round(H,2)