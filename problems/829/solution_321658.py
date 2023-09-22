def soma_h(n):
    h = 0
    for a in range(1,n+1):
        h = h + 1/a
    return round(h,2)