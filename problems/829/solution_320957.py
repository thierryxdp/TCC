def soma_h(N: int):
    H=0
    for den in range(1,N+1):
        H=H+1/den
    return round(H,2)