def soma_h(N):
    H=1
    for i in range(1,N+1):
        H=H+(1/i)
    return round(H,2)