def soma_h(n):
    H = 0
    for divisor in range(1,n+1):
        H = H + 1/n
    return round(H,2)