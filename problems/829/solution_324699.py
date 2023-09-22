def soma_h(N):
    H=0
    for n in range(1,N+1):
        H+=0.01+round(1/n, 2)
    return H