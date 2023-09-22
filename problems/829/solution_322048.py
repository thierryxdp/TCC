def soma_h(N):
    H=0
    for i in range(1,N+1):
        H=H+(1/i)
    H=round(H,2)
    return H