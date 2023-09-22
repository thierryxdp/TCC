def soma_h(n):
    h = 1
    for x in range(1,n):
        h += 1 / x
    h = round(h,2)
    return h