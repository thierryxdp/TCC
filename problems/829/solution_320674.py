def soma_h (n):
    H = 1
    for i in range (2,n+1):
        H += H + 1/n
    return round(H,2)