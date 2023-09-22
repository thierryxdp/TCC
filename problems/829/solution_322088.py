def soma_h(N):
    
    H=0

    for n in range(1,N+1):
        H=H+(1/n)
        
    return round(H,2)