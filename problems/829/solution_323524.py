def soma_h(N):
    H=0
    for k in range(1,N+1):
        H+=(1/k)
    return round(H,2)