def soma_h(N):
    H=1
    for n in range(2,N+1):
        soma=(1/n)
        H+=soma
    return round(H,2)