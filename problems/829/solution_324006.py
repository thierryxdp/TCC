def soma_h(N):
    H=0
    for varredor in range(1,N+1):
        H+=1/varredor
    return round(H,2)