def soma_h(n):
    R = 0 
    for y in range(1,n + 1):
        R += 1/y
    return round(R,2)