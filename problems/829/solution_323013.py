def soma_h(n):
    H=1
    for x in range(2,n+1):
        H=H+1/x
    return round(H,2)