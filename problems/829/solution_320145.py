def soma_H(N):
    H=0
    for elemento in range(1,N+1):
        H=H+1/elemento
    return round(H,2)