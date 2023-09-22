def soma_h(N):
    H=0
    for i in range(1,N+1):
        H+=i**-1
    return round(H,2)