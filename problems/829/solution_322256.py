def soma_h(n):
    if n==0:
        return 0
    H = 1
    for i in range(2,n+1):
        H+=1/i
    return round(H,2)