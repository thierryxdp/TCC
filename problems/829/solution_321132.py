def soma_h(N):
    V=(1/N)
    H=0
    for n in range(1,N+1):
        H+=V
    return H