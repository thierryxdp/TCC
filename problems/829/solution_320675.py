def soma_h (n):
    H = 0
    for i in range (2,n+1):
        H +=  1 + 1/n
    return round(H,2)