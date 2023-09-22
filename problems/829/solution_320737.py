def soma_h(n):
    h=0
    for i in range(1,n):
        h = h + (1/i)
    h = h + 1/n
    z = round(h,2)
    return z