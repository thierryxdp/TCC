def soma_h(n):
    h = 0
    for x in range(1,n+1):
        h += 1 / x
    h = round(h,2)
    return h