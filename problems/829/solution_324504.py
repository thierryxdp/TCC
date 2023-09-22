def soma_h(n):
    h = 0
    for x in range(0,n):
        h += 1 / x
    h = round(h,2)
    return h