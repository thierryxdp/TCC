def soma_h(n):
    h=1
    for i in range(2,n):
        h = h + (1/i)
    z = round(h,2)
    return z