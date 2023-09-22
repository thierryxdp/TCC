def soma_h(n):
    h=0
    for i in range(n+1):
        h = h + 1/i
    return round(h,2)