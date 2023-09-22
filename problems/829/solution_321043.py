def soma_h(N):
    H = 0
    for i in range(1,N):
        H = H+(1/i)
    
    return round(H, 2)