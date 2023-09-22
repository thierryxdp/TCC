def soma_h(n):
    H=0
    for i in range(n+1):
        H=H+1/i
    return round(H,2)