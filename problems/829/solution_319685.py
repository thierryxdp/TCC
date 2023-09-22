def soma_h(n):
    h=1
    for c in range(2,n+1):
        h+=1/c
    return round(h,2)